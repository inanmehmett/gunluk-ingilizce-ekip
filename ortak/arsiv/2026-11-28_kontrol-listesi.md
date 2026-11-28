# Tek sayfa kontrol listesi (24 Eki 2026)

Ekip izinde olduğu sürece her içerik **tek geçişte** bu listeyle kontrol edilir. Liste, 14 el kitabının pratikte yakaladığı hataların özetidir; el kitapları yerinde duruyor, sadece okunmuyor.

## 1. Hook (Mr. Feast)
- [ ] İlk 3 saniyede ne vadettiği belli mi?
- [ ] "İngilizce" kelimesi hook'ta geçiyor mu? (Kitlenenler hatası: geçmiyordu)
- [ ] Abartı yok: "kimsenin öğretmediği", "herkes bunu yanlış biliyor" yok.
- [ ] Takipçiye hook anketi, kamera arkası, "hangisini beğendin" yok.

## 2. İngilizce (David Kristal)
- [ ] Cümleleri ana dili İngilizce olan biri gerçekten böyle kurar mı?
- [ ] Ekrandaki alıntı, atıfta bulunulan metinde **birebir** geçiyor mu? (R03 hatası: "a new plant" metinde yoktu)
- [ ] Seviye iddiası metne ait, izleyiciye değil. "A1'i geçtin" yok; "bu metin A1" var.
- [ ] Dış kaynaklı iddia varsa: sayı, kapsam ve koşullar kaynakla aynı mı, link var mı, "tek bir çalışma" notu düşülmüş mü? (R01 hatası: 121 ↔ 120 kişi)

## 3. Türkçe ve kültür (Tomris Uyan)
- [ ] Çeviri kokuyor mu? Yüksek sesle oku; Türk bir insan bunu böyle söyler mi?
- [ ] Kültürde karşılığı olan fiil seçilmiş mi? ("çay demlemek/koymak" ✓, "çay doldurmak" ✗)
- [ ] Aynı İngilizce kalıp, paketler arasında **tek** Türkçe karşılıkla gidiyor mu? (make = hazırlamak; bir pakette "yapmak" olmaz)
- [ ] Deyimsel çeviri anlamı daraltıyor mu? ("go away = çekip gitmek" ✗ → "gitmek, uzaklaşmak" ✓)
- [ ] Kural 10: "Türkçesi" bölümü cevap anahtarıdır — önce İngilizce okunsun, Türkçe aşağıda kalsın.

## 4. Görsel (Jony Ayv)
- [ ] 1 / l / I testi: rakamlar `lnum`+`tnum` ile mi çizildi? ("A1" → "Al" okunmasın)
- [ ] En uzun satır kutuya sığıyor mu, kutu güvenli bandın (≈850 px) içinde mi?
- [ ] Emoji render oldu mu (kutu değil)?
- [ ] Yan yana gelecek reeller (ızgarada komşu) farklı kutu düzeni ve farklı klip kullanıyor mu?

## 5. Kurgu ve zaman (Walter Marş)
- [ ] Ekrandaki metnin okunma süresi, videonun süresinden kısa mı? (Rahat okuma: ~12 karakter/saniye)
- [ ] Liste ilk kareden itibaren görünüyor mu? (Sonradan belirmesi izleyiciyi kaçırıyor)
- [ ] 9. saniye düşüşü: süre gerçekten gerekli mi, kısaltılabilir mi?

## 6. Psikoloji (Daniel Kahraman)
- [ ] İzleyiciyi utandıran bir cümle var mı? ("hâlâ bilmiyorsan…" ✗)
- [ ] Kaydetme ve gönderme için somut bir sebep verilmiş mi?
- [ ] Yorum daveti, izleyicinin kendi beyanına dayanıyor mu? ("anladıysan ✅ bırak" ✓)

## 7. Şeytanın avukatı (Charlie Hunger)
- [ ] **"Mehmet ne yakalardı?"** — `ortak/mehmet_yakaladi.md` dosyasındaki 11 hataya bak; aynısının yenisi var mı?
- [ ] Reklam üslubu var mı? Uygulamanın özelliği anlatılmaz, varlığı gösterilir.

## 8. Son kapı (Sal Kaan)
- [ ] Ekrandaki metin ile `PAKET.md` birebir aynı mı?
- [ ] Açıklama ile ekran birbiriyle çelişiyor mu? (H02 hatası: kapak ile açıklama farklıydı)
- [ ] Takvimde günü, saati, klibi yazıldı mı? Klip son 3 haftada kullanılmış mı?
- [ ] Sürüm satırı düşüldü mü?

---

## Ekip ne zaman izinden döner?

Alt ajanlı çok rollü inceleme **sadece** şu dört durumda açılır:
1. Yeni bir seri ya da ilk kez denenen bir format.
2. Dış kaynaklı bir iddia içeren içerik (araştırma, istatistik).
3. Mehmet bir içeriğe itiraz etti ve sebebi anlaşılmadı.
4. Aylık ekip sağlık kontrolü.

Çağrılırken prompt'ta hangi dosyaların okunacağı tek tek yazılır; ajan kendi başına arama yapmaz.
