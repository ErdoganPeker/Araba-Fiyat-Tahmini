# 🚗 Araba Fiyat Tahmini — Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-FF6600?style=flat)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=flat&logo=tensorflow&logoColor=white)

> Marka, model, yıl, kilometre, yakıt türü ve vites gibi özelliklere göre ikinci el araç fiyatını tahmin eden makine öğrenmesi ve derin öğrenme projesi.

---

## ✨ Özellikler

- Kapsamlı Keşifsel Veri Analizi (EDA) ve interaktif görselleştirme
- Birden fazla ML modelinin karşılaştırmalı değerlendirmesi (Linear Regression, Random Forest, XGBoost vb.)
- Derin öğrenme modeli ile fiyat tahmini
- Eğitilmiş en iyi model pickle formatında kaydedilmiş (`best_model.pkl`)
- Tüm model sonuçları karşılaştırmalı raporlama (`model_results.csv`)

---

## 🛠️ Teknoloji Yığını

| Kategori | Araçlar |
|---|---|
| ML / DL | scikit-learn, XGBoost, TensorFlow / Keras |
| Veri İşleme | Pandas, NumPy |
| Görselleştirme | Matplotlib, Seaborn |
| Model Yönetimi | Pickle |
| Ortam | Jupyter Notebook |

---

## 📂 Proje Yapısı

```
Araba-Fiyat-Tahmini/
├── car-price-prediction.ipynb   # Ana analiz ve model eğitim notebook'u
├── car details v4.csv           # Ham veri seti (Türk ikinci el araç pazarı)
├── best_model.pkl               # Eğitilmiş en iyi model
└── model_results.csv            # Tüm modellerin karşılaştırmalı sonuçları
```

---

## 📊 Temel Sonuçlar

- Türk ikinci el araç pazarına ait gerçek veri seti üzerinde çalışıldı
- Marka, model, yıl, kilometre, yakıt türü ve şanzıman türü bağımsız değişken olarak kullanıldı
- En iyi performans gösteren model pickle dosyası olarak dışa aktarıldı; doğrudan tahmin için kullanılabilir
- Model karşılaştırma sonuçları `model_results.csv` dosyasında R², RMSE ve MAE metrikleriyle raporlandı

---

## 🚀 Başlangıç

### Gereksinimler

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow jupyter
```

### Çalıştırma

```bash
git clone https://github.com/ErdoganPeker/Araba-Fiyat-Tahmini.git
cd Araba-Fiyat-Tahmini
jupyter notebook car-price-prediction.ipynb
```

### Eğitilmiş Modeli Kullanma

```python
import pickle, pandas as pd

with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

sample = pd.DataFrame([{
    "brand": "Toyota", "model": "Corolla", "year": 2019,
    "km": 45000, "fuel": "Benzin", "transmission": "Otomatik"
}])
print(f"Tahmini Fiyat: {model.predict(sample)[0]:,.0f} TL")
```

---

## 👤 Geliştirici

**Erdoğan Yasin Peker**
[GitHub](https://github.com/ErdoganPeker) · [LinkedIn](https://www.linkedin.com/in/erdogan-yasin-peker-b107ba24b/)
