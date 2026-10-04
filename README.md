# 💱 Döviz Çevirici

Python kullanılarak geliştirilmiş, güncel döviz kurlarını internet üzerinden alarak **Türk Lirası ile farklı para birimleri arasında dönüşüm** yapabilen terminal tabanlı döviz çevirici uygulaması.

Proje, `yfinance` kütüphanesini kullanarak döviz kurlarını alır ve kullanıcıya seçtiği para biriminde işlem yapma imkânı sunar.

## 🚀 Özellikler

* Güncel döviz kurlarını internet üzerinden alma
* Türk Lirası ↔ yabancı para birimi dönüşümü
* Terminal üzerinden kolay kullanım
* Kullanıcıdan alınan miktarı otomatik olarak hesaplama
* Hatalı girişlerde kullanıcıyı uyarma
* Sayısal olmayan girişleri kontrol etme
* 24 farklı para birimi seçeneği

## 💰 Desteklenen Para Birimleri

Uygulamada aşağıdaki para birimleri bulunmaktadır:

1. 🇺🇸 Amerikan Doları (USD)
2. 🇪🇺 Euro (EUR)
3. 🇬🇧 İngiliz Sterlini (GBP)
4. 🇨🇭 İsviçre Frangı (CHF)
5. 🇸🇦 Suudi Arabistan Riyali (SAR)
6. 🇯🇵 Japon Yeni (JPY)
7. 🇨🇦 Kanada Doları (CAD)
8. 🇦🇺 Avustralya Doları (AUD)
9. 🇷🇺 Rus Rublesi (RUB)
10. 🇨🇳 Çin Yuanı (CNY)
11. 🇰🇼 Kuveyt Dinarı (KWD)
12. 🇶🇦 Katar Riyali (QAR)
13. 🇦🇪 Birleşik Arap Emirlikleri Dirhemi (AED)
14. 🇸🇪 İsveç Kronu (SEK)
15. 🇳🇴 Norveç Kronu (NOK)
16. 🇩🇰 Danimarka Kronu (DKK)
17. 🇵🇱 Polonya Zlotisi (PLN)
18. 🇷🇴 Rumen Leyi (RON)
19. 🇨🇿 Çek Korunası (CZK)
20. 🇧🇬 Bulgar Levası (BGN)
21. 🇮🇳 Hindistan Rupisi (INR)
22. 🇲🇽 Meksika Pesosu (MXN)
23. 🇰🇷 Güney Kore Wonu (KRW)
24. 🇧🇷 Brezilya Reali (BRL)

## 🛠️ Kullanılan Teknolojiler

* **Python**
* **yfinance**

`yfinance`, döviz kuru verilerini almak için kullanılmaktadır. Örneğin Amerikan Doları/Türk Lirası kuru `USDTRY=X` sembolü üzerinden alınır.

## 📦 Kurulum

Öncelikle bilgisayarınızda Python'un kurulu olduğundan emin olun.

Daha sonra terminali açarak `yfinance` kütüphanesini yükleyin:

```bash
pip install yfinance
```

Projeyi bilgisayarınıza indirdikten sonra proje klasörüne girin:

```bash
cd proje-klasoru
```

Programı çalıştırmak için:

```bash
python main.py
```

> Eğer Python dosyanızın adı farklıysa `main.py` yerine kendi dosya adınızı yazabilirsiniz.

## ▶️ Kullanım

Program çalıştırıldığında kullanıcıdan işlem yapmak istediği döviz biriminin numarası istenir.

Örneğin:

```text
İşlem yapmak istediğini döviz biriminin numarasını giriniz:

1. Amerikan Doları
2. Euro
3. İngiliz Sterlini
...
24. Çıkış
```

Bir para birimi seçildikten sonra iki farklı işlem yapılabilir:

```text
1. Amerikan Doları ➔ Türk Lirası
2. Türk Lirası ➔ Amerikan Doları
3. Çıkmak için basınız.
```

### Örnek

Kullanıcı `1` numaralı işlemi seçerse:

```text
Çevirmek istediğiniz miktarı giriniz:
100
```

Program güncel kura göre yaklaşık sonucu hesaplar:

```text
Miktarınız: 4250.00 TL
```

Tersi yönde de TL'den seçilen döviz birimine dönüşüm yapılabilir. Kodda bu işlem, seçilen miktarın kura bölünmesiyle gerçekleştirilmektedir.

## ⚠️ Hatalı Giriş Kontrolü

Program, kullanıcı yanlış bir işlem numarası girdiğinde uyarı verir:

```text
Hatalı işlem geçerli bir veri giriniz.
```

Ayrıca miktar yerine sayı olmayan bir değer girildiğinde `ValueError` kontrolü ile kullanıcı tekrar sayı girmeye yönlendirilir.

## 📁 Proje Yapısı

```text
doviz-cevirici/
│
├── main.py
└── README.md
```

* `main.py` → Döviz çevirici uygulamasının Python kodu
* `README.md` → Proje hakkında açıklamalar ve kullanım bilgileri

## 📌 Projenin Amacı

Bu proje Python öğrenme sürecinde geliştirilmiş bir **döviz çevirici uygulamasıdır**.

Proje sayesinde;

* Fonksiyon oluşturma
* `while` döngüsü kullanma
* `if / elif / else` yapıları
* `try / except` ile hata yakalama
* Kullanıcıdan `input()` ile veri alma
* `float()` ve `int()` kullanımı
* Liste kullanımı
* API/veri kaynağından güncel veri alma
* Döviz kuru üzerinden matematiksel dönüşüm yapma

gibi Python konularında pratik yapılmıştır.

## 🔮 Gelecekte Eklenebilecek Özellikler

* 📊 Kur geçmişini gösterme
* 📈 Döviz grafiklerini gösterme
* 🔄 Birden fazla dövizi aynı anda karşılaştırma
* 💾 Yapılan işlemleri kaydetme
* 🖥️ Grafiksel kullanıcı arayüzü (GUI)
* 🌐 Web tabanlı versiyon
* 📱 Mobil uygulama versiyonu
* ⭐ Favori para birimleri sistemi

## 👩‍💻 Geliştirici

**Büşra**

Python öğrenme sürecinde geliştirilmiştir.

---

⭐ Projeyi faydalı bulduysanız GitHub'da yıldız vermeyi unutmayın!
