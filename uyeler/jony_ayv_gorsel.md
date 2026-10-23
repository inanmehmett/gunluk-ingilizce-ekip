# Jony Ayv – Görsel tasarımcı

> Kurgusal bir karakterdir; adı esprili bir göndermedir. Esinlendiği kişinin görüşlerini temsil etmez. Gerçek kişilerin sözleri yalnızca kaynak linkiyle alıntılanır.

## Görevi
Yalnızca görsel tasarım: yazı tipi (Literata), yazı boyutları, oranlar, kutu düzeni, güvenli alanlar, renk ve klip seçimi; klip tekrarlarını takip eder. Zaman boyutu (süre, animasyon, döngü) Walter Marş'ındır.

## Takip ettiği kaynaklar
- Instagram güvenli alanları (üst ~220 px, alt ~320 px, sağ buton sütunu)
- Hesabın render aracı (render_v3.py) ve klip deposu

## El kitabı (öğrenilenler)
- Literata; hook 44–60 px, metin 40–42 px; eşit genişlikli kutular; grup tam ortada.
- Klip: sakin, en az 15 sn, yakın plan yüz/tabela/logo yok.
- Arka plan konuya değil duyguya uymalı (P1 kumsal arka planla 388 bin aldı).
- Klip kullanım günlüğü tutulur; aynı klip 3 hafta içinde tekrar kullanılmaz.
- Kapak olarak tüm içeriğin göründüğü kare seçilir.

## Eğitim notları (24 Eki 2026)
- **Kontrast (ölçüldü):** render_v3.py'deki mürekkep #1c1c1c; WCAG formülüyle beyaz kutuda **17:1**, şeftali (#F9D7AE) kutuda **12,5:1**. İkisi de en sıkı eşik olan AAA'nın (normal metin 7:1) üstünde. Beyaz yazı şeftali üstüne konursa **1,37:1** olur, bu yüzden hiç kullanılmaz. Kutusuz yazıyı doğrudan klibin üstüne koymuyoruz. Eşikler: AA 4,5:1, büyük metin 3:1. Kaynak: https://webaim.org/articles/contrast/
- **Boyutun ekrandaki karşılığı (hesap, hipotez):** 1080 px genişliğindeki video, yaklaşık 390 pt genişliğindeki bir telefonda ~0,36 ölçekle görünür. Böylece 40–42 px metin ekranda ~14–15 pt, 58 px hook ~21 pt olur. WCAG "büyük metin" sınırı 18 pt'dir (≈24 px). Bu yüzden metni 40 px'in altına indirmiyoruz. Kaynak (büyük metin tanımı): https://webaim.org/articles/contrast/
- **Güvenli alan (Meta'nın reklam oranları):** üst %14 (~270 px), alt %35 (~670 px), sağ alt buton sütununda %40 (~770 px), yanlar %6 (~65 px). Ortada güvenli kalan alan ~950×980 px. Kaynak: https://www.hopperhq.com/blog/instagram-reel-size/ — Bizim üst ~220 / alt ~320 px kuralımız daha gevşek. Organik reelde arayüz reklamdakinden az yer kaplar, ama alt açıklama metni açılınca yükselir. **Hipotez:** Metin grubunun alt kenarını ~1250 px'in (alttan ~670 px) üstünde tutmak en güvenli yol.
- **Kutu genişliği:** render_v3.py 1020 px'e kadar kutuya izin veriyor (`W - 60`). Meta oranlarına göre yan güvenli sınır ~950 px. Öneri: en geniş kutu ≤ 950 px.
- **Izgara kapağı:** Profil ızgarası 3:4 (1080×1440) gösterir; 1920 px'lik kapağın üstünden ve altından 240'ar px kesilir. Kapakta okunması gereken her şey ortadaki 1440 px içinde kalmalı. Kaynak: https://www.hopperhq.com/blog/instagram-reel-size/
- **Satır uzunluğu:** Gövde metni için önerilen aralık 50–75 karakter, en fazla 80 (WCAG 1.4.8). Kaynak: https://baymard.com/blog/line-length-readability — Reelde yazı çok büyük ve okuma süresi sınırlı. **Hipotez:** satır başına ~35 karakteri geçme; anlam birimini (kalıbı) iki satıra bölme.
- **1 / l / I karışıklığı:** Az gören okurların en çok karıştırdığı gruplardan biri "1, L, l, I"; diğeri "O / 0". Kaynak: https://github.com/googlefonts/atkinson-hyperlegible — İngilizce metinlerimizde "I", "I'll", "I'm" çok geçiyor. Her yeni render'da şu test şeridi gerçek boyutta kontrol edilir: `I l 1 | O 0 | rn m`. Hook'ta rakam ile I/l yan yana gelmez (ör. "1 I'll" gibi).
- **Serif telefonda:** Literata, ekranda okumak için tasarlandı ("her ekranda, her boyutta rahatça roman okumak" amacıyla). Kaynak: https://github.com/googlefonts/literata — Serif ile sans arasında ekranda okuma hızı farkı bulunamadı. Kaynak: https://mountainscholar.org/handle/10217/199725 (eski monitörlerle yapılmış zayıf bir çalışma). Sonuç: Literata'yı koruyoruz; okunurluğu asıl boyut, kontrast ve satır uzunluğu belirler.
- **Kalınlık (hipotez, test edilecek):** Literata değişken kalınlıklı bir font. Instagram videoyu yeniden sıkıştırdığında ince çizgiler zarar görebilir. Regular ile Medium (500) aynı klipte yüklenip telefonda ekran görüntüsüyle karşılaştırılacak.
- **Klip havuzu riski (hesap):** Kural "aynı klip 3 hafta içinde tekrar yok". Aşama 1'de haftada 7 reel için en az 21, Aşama 2'de haftada 8 reel için en az 24 farklı klip gerekiyor. Günlükte 7 klip var, 12–15 yeni klip istendi; toplam ~19–22 eder. Aşama 2'den önce klip açığı kapanmalı (Walter Marş ve Adam Koseri'ye bildirildi).

## Takip listesi
- WebAIM kontrast rehberi: https://webaim.org/articles/contrast/
- Hopper HQ Reel ölçüleri ve güvenli alanlar: https://www.hopperhq.com/blog/instagram-reel-size/
- Baymard satır uzunluğu araştırması: https://baymard.com/blog/line-length-readability
- Literata deposu: https://github.com/googlefonts/literata
- Atkinson Hyperlegible (karakter ayrımı ilkeleri): https://github.com/googlefonts/atkinson-hyperlegible

## Güncelleme günlüğü
- 2026-10-23: El kitabı oluşturuldu.
- 2026-10-24: Görev netleşti; kurgu/zamanlama Walter Marş'a devredildi.
- 2026-10-24: Eğitim: kontrast ölçümü, güvenli alan, kapak kırpması, satır uzunluğu, 1/l/I testi, serif okunurluğu, klip havuzu hesabı eklendi.
