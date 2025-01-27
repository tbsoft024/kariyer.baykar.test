1. Manuel Testler: Manuel Test Dökümü doc ve pdf olarak hazırlanmıştır.

2. Otomasyon Testleri:
    Kullannılan yapı :
      Python [Opsiyonel]
      a. Unittest/PyUnit - Pytest ile yapıldı
      b. BeautifulSoup - Kullanıldı.
      c. Selenium /WebDriver/WebDriverWait/ExpectedConditions - Kullanıldı.
      d. Robot Framework - Kullanılmadı.

Otomasyonu çalıştırılması ve yüklenmesi gereken kodlarıda burada hazır olması açısından paylaşıyorum.
  pip install pytest
  pip install webdriver-manager
  pip install pytest-html

raporlu almak isterseniz aşağıdaki kod ile çalıştırabilirsiniz.
  pytest --html=report.html --self-contained-html  

normal 
  pytest -v

<< Sorularınızı anladığım kadarı ile otomasyonu hazırlamaya çalıştım. Ama C sorusunu anlayamadığım için yarıda bıraktım. Kusura bakmayınız. >>

      " C. Ziyaretçi/Kullanıcı kariyer.baykartech sitesinde açık pozisyonlarda birim filtreleme ve pozisyon arama
      yapabilmeli. Data-Driven kullanımına dikkat edilmelidir
      a. Pozisyon otomasyonu dinamik yapıda olmalıdır. Mevcut birim ve pozisyonlar siteden çekilmeli
      ve verilen input ile eşleştirilmelidir. Otomasyonun filtreleme ve arama sonucu tıkladığı
      pozisyonun başlığı ile inputa girilen veri eşleşmeli veya içermelidir. "


3.Yük/ Performans Testleri: 
Bir web sitesi için daha önceden performans tecrübem olmadı.
Mantık olarak User sayısı 1 - 10 - 100 gibi istek gönderip server cevap verme ms bakılarak analiz yapıldığını biliyorum.
