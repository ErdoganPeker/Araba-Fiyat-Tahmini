🔹 🔸 **ARABA FİYATLARI TAHMİNİ PROJESİ** 🔸 🔹

Otomobil fiyatları, birçok faktörden etkilenir; markası, modeli, üretim yılı, kilometresi, yakıt türü, vites tipi ve ek donanımlar gibi. Bu faktörlerin doğru şekilde analiz edilmesi, alıcılar için daha bilinçli satın alma kararları almayı ve satıcılar için rekabetçi fiyatlandırma stratejileri geliştirmeyi sağlar. Ancak, otomobil fiyatları genellikle çok dinamik ve karmaşık bir yapıdadır, bu yüzden doğru fiyat tahminleri yapmak her zaman kolay değildir.

Bu proje, araçların teknik özellikleri, performans kriterleri ve pazarla ilgili çeşitli faktörleri içeren bir veri setini kullanarak, araçların piyasa değerini doğru bir şekilde tahmin etmeyi amaçlamaktadır. Bu veri setinde yer alan bilgiler ile, doğru fiyat tahminleri yapmak için güçlü bir makine öğrenmesi modeli oluşturulması hedeflenmiştir.

Bu çalışmanın temel amacı, araba fiyatlarını etkileyen faktörleri analiz etmek ve araçların satış fiyatlarını doğru bir şekilde tahmin edebilen bir model geliştirmektir. Projede istatistiksel analizler, makine öğrenmesi algoritmaları ve derin öğrenme teknikleri kullanılarak tahminler yapılacak ve elde edilen sonuçlar, otomotiv sektörü ve bireysel kullanıcılar için değerli bilgiler sunacaktır.

🔰 **VERİ SETİ**  
Proje, araçların teknik özelliklerine dair çok çeşitli bilgileri içeren bir veri setine dayanıyor. Bu veri seti, araçların markası, modeli, üretim yılı, kilometresi, yakıt türü, vites tipi gibi bilgileri içerir. Bu verilerle araç fiyatlarını tahmin etmek için çeşitli makine öğrenmesi modelleri uygulanacaktır.

🔰 **KULLANILAN ALGORİTMALAR**  
Proje kapsamında, araç fiyatlarını tahmin etmek için çeşitli makine öğrenmesi algoritmaları kullanılacaktır. Bu algoritmalar arasında:

- **Lineer Regresyon**
- **Ridge Regresyon**
- **Lasso Regresyon**
- **Elastic Net**
- **Destek Vektör Regresyonu (SVR)**
- **Rastgele Orman Regresyonu (Random Forest)**
- **Gradient Boosting Regresyonu**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **KNN Regresyonu** 

ve diğer birçok farklı model bulunmaktadır.

🔰 **EĞİTİM VE DEĞERLENDİRME METRİKLERİ**  
Eğitim sırasında k-fold çapraz doğrulama yöntemi kullanılacak ve her modelin doğruluk oranları, R² skoru, MAE, MSE gibi metriklerle değerlendirilecektir. Bu metrikler, modellerin performansını karşılaştırmak ve en iyi tahmin modelini seçmek için kullanılacaktır. Ayrıca, aşağıdaki gibi sonuçlar elde edilmiştir:

İşte sonuçların **e** cinsinden yazılmış hali:

| Model               | RMSE        | MAE         | R²        |
|---------------------|-------------|-------------|-----------|
| **CatBoost**         | 4.143331e-05 | 2.089880e-05 | 0.961134  |
| **Random Forest**    | 4.961388e-05 | 2.444697e-05 | 0.944271  |
| **XGBoost**          | 5.506966e-05 | 2.456692e-05 | 0.931341  |
| **Gradient Boosting**| 5.081543e-05 | 2.317647e-05 | 0.941539  |
| **LightGBM**         | 6.041947e-05 | 2.807798e-05 | 0.917353  |
| **KNN Regressor**    | 6.545520e-05 | 3.206239e-05 | 0.903002  |
| **Ridge Regression** | 9.726454e-05 | 5.745752e-05 | 0.785817  |
| **Lasso Regression** | 9.767336e-05 | 5.723580e-05 | 0.784013  |
| **Linear Regression**| 9.767393e-05 | 5.723599e-05 | 0.784011  |
| **Elastic Net**      | 1.096777e-06 | 6.513339e-05 | 0.727660  |
| **SVR**              | 2.310354e-06 | 1.268284e-06 | -0.208459 |

