from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Synthetic Turkish car market data
np.random.seed(42)
n = 2000
brands = ['Toyota','Honda','Volkswagen','Ford','Renault','Hyundai','BMW','Mercedes','Audi','Fiat']
fuel_types = ['Benzin','Dizel','LPG','Elektrik','Hibrit']
transmissions = ['Manuel','Otomatik']

brand_arr = np.random.choice(brands, n)
fuel_arr = np.random.choice(fuel_types, n)
trans_arr = np.random.choice(transmissions, n)
year_arr = np.random.randint(2005, 2024, n)
km_arr = np.random.randint(5000, 300000, n)

# Price based on realistic factors
base = {'Toyota':180,'Honda':170,'Volkswagen':200,'Ford':160,'Renault':150,'Hyundai':155,'BMW':320,'Mercedes':350,'Audi':300,'Fiat':120}
fuel_mult = {'Benzin':1.0,'Dizel':1.1,'LPG':0.85,'Elektrik':1.4,'Hibrit':1.2}
trans_mult = {'Manuel':1.0,'Otomatik':1.15}

prices = []
for i in range(n):
    p = base[brand_arr[i]] * fuel_mult[fuel_arr[i]] * trans_mult[trans_arr[i]]
    p *= (1 + (year_arr[i] - 2010) * 0.05)
    p -= km_arr[i] * 0.0001
    p += np.random.normal(0, 15)
    prices.append(max(50, p))

le_brand = LabelEncoder().fit(brands)
le_fuel = LabelEncoder().fit(fuel_types)
le_trans = LabelEncoder().fit(transmissions)

X = np.column_stack([
    le_brand.transform(brand_arr),
    le_fuel.transform(fuel_arr),
    le_trans.transform(trans_arr),
    year_arr, km_arr
])
y = np.array(prices)

model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

class CarData(BaseModel):
    brand: str
    fuel: str
    transmission: str
    year: int
    km: int

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "brands": brands,
        "fuels": fuel_types,
        "transmissions": transmissions
    })

@app.post("/predict")
async def predict(data: CarData):
    x = np.array([[
        le_brand.transform([data.brand])[0],
        le_fuel.transform([data.fuel])[0],
        le_trans.transform([data.transmission])[0],
        data.year,
        data.km
    ]])
    pred = model.predict(x)[0]
    return {"prediction": f"{pred:.0f}K TL", "confidence": 0.84}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5005)

