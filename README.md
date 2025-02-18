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

| Model               | RMSE        | MAE         | R²        |
|---------------------|-------------|-------------|-----------|
| **CatBoost**         | 420,839.37  | 208,912.69  | 0.9599    |
| **Random Forest**    | 497,590.73  | 244,230.84  | 0.9439    |
| **XGBoost**          | 511,870.54  | 245,187.73  | 0.9407    |
| **Gradient Boosting**| 516,620.32  | 245,088.07  | 0.9396    |
| **LightGBM**         | 605,875.79  | 284,540.01  | 0.9169    |
| **KNN Regressor**    | 654,552.03  | 320,623.90  | 0.9030    |
| **Ridge Regression** | 972,645.39  | 574,575.16  | 0.7858    |
| **Lasso Regression** | 976,725.07  | 572,351.02  | 0.7840    |
| **Linear Regression**| 976,739.27  | 572,359.94  | 0.7840    |
| **Elastic Net**      | 1,212,411.51| 691,711.30  | 0.6672    |
| **SVR**              | 2,310,353.63| 1,268,283.54| -0.2085   |


