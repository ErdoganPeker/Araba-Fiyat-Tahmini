from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
import pandas as pd
import os
import re
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import uvicorn

app = FastAPI()
_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(_dir, "templates"))

# Real Indian used-car market data (repo's own dataset — the pickled
# best_model(1).pkl ships without its preprocessing pipeline, so this
# retrains an equivalent model directly from the real CSV instead).
df = pd.read_csv(os.path.join(_dir, "..", "car details v4.csv"))
df["Fuel Type"] = df["Fuel Type"].str.split(" + ").str[0]


def _extract_number(value):
    """Pull the first numeric token out of strings like '1198 cc',
    '87 bhp @ 6000 rpm' or '109 Nm @ 4500 rpm'. Returns NaN if absent."""
    if pd.isna(value):
        return np.nan
    match = re.search(r"[-+]?\d*\.?\d+", str(value))
    return float(match.group()) if match else np.nan


# --- Parse compound string columns into numeric features -------------------
df["engine_cc"] = df["Engine"].apply(_extract_number)
df["max_power_bhp"] = df["Max Power"].apply(_extract_number)
df["max_torque_nm"] = df["Max Torque"].apply(_extract_number)

# --- Impute missing values (median for numeric, mode for categorical) ------
numeric_fill_cols = [
    "engine_cc", "max_power_bhp", "max_torque_nm",
    "Length", "Width", "Height", "Seating Capacity", "Fuel Tank Capacity",
]
for col in numeric_fill_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_fill_cols = [
    "Make", "Fuel Type", "Transmission", "Location", "Color",
    "Owner", "Seller Type", "Drivetrain",
]
for col in categorical_fill_cols:
    df[col] = df[col].fillna(df[col].mode().iloc[0])

# --- Dropdown option lists for the UI (sorted unique values) ---------------
brands = sorted(df["Make"].unique().tolist())
fuel_types = sorted(df["Fuel Type"].unique().tolist())
transmissions = sorted(df["Transmission"].unique().tolist())
locations = sorted(df["Location"].unique().tolist())
colors = sorted(df["Color"].unique().tolist())
owners = sorted(df["Owner"].unique().tolist())
seller_types = sorted(df["Seller Type"].unique().tolist())
drivetrains = sorted(df["Drivetrain"].unique().tolist())

# --- Label encoders for every categorical feature ---------------------------
le_brand = LabelEncoder().fit(brands)
le_fuel = LabelEncoder().fit(fuel_types)
le_trans = LabelEncoder().fit(transmissions)
le_location = LabelEncoder().fit(locations)
le_color = LabelEncoder().fit(colors)
le_owner = LabelEncoder().fit(owners)
le_seller = LabelEncoder().fit(seller_types)
le_drivetrain = LabelEncoder().fit(drivetrains)

FEATURE_NAMES = [
    "brand", "fuel", "transmission", "year", "km",
    "location", "color", "owner", "seller_type", "drivetrain",
    "engine_cc", "max_power_bhp", "max_torque_nm",
    "length", "width", "height", "seating_capacity", "fuel_tank_capacity",
]

X = np.column_stack([
    le_brand.transform(df["Make"]),
    le_fuel.transform(df["Fuel Type"]),
    le_trans.transform(df["Transmission"]),
    df["Year"],
    df["Kilometer"],
    le_location.transform(df["Location"]),
    le_color.transform(df["Color"]),
    le_owner.transform(df["Owner"]),
    le_seller.transform(df["Seller Type"]),
    le_drivetrain.transform(df["Drivetrain"]),
    df["engine_cc"],
    df["max_power_bhp"],
    df["max_torque_nm"],
    df["Length"],
    df["Width"],
    df["Height"],
    df["Seating Capacity"],
    df["Fuel Tank Capacity"],
])
y = df["Price"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GradientBoostingRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# --- Real test-set performance (replaces the old hard-coded 0.84) ----------
model_r2 = float(r2_score(y_test, model.predict(X_test)))

# --- Feature importances, descending -----------------------------------
feature_importance = sorted(
    (
        {"feature": name, "importance": float(score)}
        for name, score in zip(FEATURE_NAMES, model.feature_importances_)
    ),
    key=lambda item: item["importance"],
    reverse=True,
)

# --- Per-brand average price stats (for brand comparison) -------------------
_brand_stats = df.groupby("Make")["Price"].agg(["mean", "count"])
brand_avg_price = {
    make: {"avg_price": float(row["mean"]), "count": int(row["count"])}
    for make, row in _brand_stats.iterrows()
}


class CarData(BaseModel):
    brand: str
    fuel: str
    transmission: str
    year: int
    km: int
    location: str
    color: str
    owner: str
    seller_type: str
    drivetrain: str
    engine_cc: float
    max_power_bhp: float
    max_torque_nm: float
    length: float
    width: float
    height: float
    seating_capacity: int
    fuel_tank_capacity: float


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "brands": brands,
        "fuels": fuel_types,
        "transmissions": transmissions,
        "locations": locations,
        "colors": colors,
        "owners": owners,
        "seller_types": seller_types,
        "drivetrains": drivetrains,
    })


@app.post("/predict")
async def predict(data: CarData):
    x = np.array([[
        le_brand.transform([data.brand])[0],
        le_fuel.transform([data.fuel])[0],
        le_trans.transform([data.transmission])[0],
        data.year,
        data.km,
        le_location.transform([data.location])[0],
        le_color.transform([data.color])[0],
        le_owner.transform([data.owner])[0],
        le_seller.transform([data.seller_type])[0],
        le_drivetrain.transform([data.drivetrain])[0],
        data.engine_cc,
        data.max_power_bhp,
        data.max_torque_nm,
        data.length,
        data.width,
        data.height,
        data.seating_capacity,
        data.fuel_tank_capacity,
    ]])
    pred = max(0, model.predict(x)[0])

    brand_stats = brand_avg_price.get(data.brand, {"avg_price": 0.0, "count": 0})

    return {
        "prediction": f"₹ {pred:,.0f}",
        "predicted_price_numeric": round(float(pred), 2),
        "confidence": round(model_r2, 4),
        "feature_importance": feature_importance,
        "model_r2": round(model_r2, 4),
        "brand_avg_price": {
            "brand": data.brand,
            "avg_price": round(brand_stats["avg_price"], 2),
            "count": brand_stats["count"],
        },
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5005)
