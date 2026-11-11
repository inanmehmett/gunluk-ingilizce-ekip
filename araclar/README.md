# Araçlar (üretim hattı)

Bu klasör olmadan yeni bir oturumda hiçbir şey üretilemez. Konteyner her oturumda sıfırlanır; kalıcı olan tek yer bu repo.

## Kurulum (yeni oturumda ilk iş)
```
git clone https://github.com/inanmehmett/gunluk-ingilizce-ekip
mkdir -p /home/claude/fonts/dl && cp gunluk-ingilizce-ekip/araclar/fonts/Literata.ttf /home/claude/fonts/dl/
```
Noto Color Emoji sistemde kurulu (`/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf`).

## reels/render_v3.py
`spec.json` + klip → 1080x1920, 30 fps mp4 + önizleme png.
```
SLOW=0.75 PUSH=0.04 python3 render_v3.py spec.json /mnt/user-data/uploads/IMG_XXXX.MOV cikti.mp4 <baslangic_sn> <sure_sn> prev.png
```
- `SLOW`: klibi yavaşlatır (0,75 = sakin). `PUSH`: Walter'ın "Görünmez Dikiş" imzası, arka planda 1→1,04→1 sinüs zoom.
- Rakamlar `lnum`+`tnum` ile çiziliyor (yoksa "A1" → "Al" okunuyor).
- Dosya 30 MB'ı aşarsa crf 24 ile yeniden kodla.

## Ekran alanı (Reels, 1080x1920) — 6 Kas 2026, Mehmet'in isteği
Instagram arayüzü videonun üstüne biner. Resmî Meta ölçüsü yayımlanmadı; aşağıdakiler üç bağımsız rehberin ortak, temkinli değeridir (Hopper HQ, Postfast, TryMyPost, 2026).
| Bölge | Piksel (y) | Ne olur | Kural |
|---|---|---|---|
| Üst | 0–270 | "Reels" başlığı, kamera simgesi | Metin yok |
| **Güvenli bant** | **270–1200** | Hiçbir şey binmez | Hook, metin, Türkçe etiket burada |
| Yarı güvenli | 1200–1500 | Açıklama uzayınca ve ses satırı buraya çıkabilir | Kritik metin yok |
| Alt | 1500–1920 | Kullanıcı adı, açıklama, ses | Metin yok |
| Sağ sütun | x>910, y 1000–1750 | Beğeni, yorum, gönder, kaydet | Metin girmez |
| Yanlar | x<65, x>1015 | Telefon kenarı, kırpma | Kutu taşmaz |
| Profil ızgarası | 240–1680 (3:4 orta kırpma) | Ilk kare kapak olur | Hook bu bandın içinde ve okunur |
`render_v3.py` grubu güvenli bandın ortasına koyar (çerçevenin değil), sığmazsa ya da kutu 950 px'ten genişse durur, sağ sütuna giren satırı uyarır. Bant değiştirmek gerekirse spec'e `safe_top` / `safe_bottom` yazılır.
Sığmıyorsa sıra: satırı kısalt → punto 42→40 → pad küçült; bandı genişletme.

## reels/paragraf_orijinal.py (11 Kas 2026) — GEÇERLİ PARAGRAF ŞABLONU
15 Eki orijinalinin ölçüleriyle paragraf reeli + isteğe bağlı kelimeye dokunma animasyonu. `python3 paragraf_orijinal.py spec.json klip.mp4 cikti.mp4 [onizleme_dizini]`; font yolu `LITERATA` ortam değişkeni. Örnek spec: `icerik/2026-11-15_reel_el_sallama/spec_v3.json`.

## reels/ladder.py
Seviye merdiveni overlay'i (A1→B2 şeridi + emoji'li hook).
`python3 ladder.py <basamak> <klip> <baslangic> <sure> cikti.mp4`

## carousel/build.py + data.py
`data.py` tüm set metinlerini tutar (tek doğru kaynak). `build_sel.py KOD KOD` sadece seçilen setleri yeniden üretir.
Görseller `gunluk-ingilizce-carousel` (public) reposuna kopyalanır; Metricool raw.githubusercontent.com linkiyle çeker.

## carousel/duzelt_overlay.py (4 Kas)
`build.py` repoda olmayan `gen.py`'ye bağlı; set baştan üretilemiyor. Tek kart düzeltmesi: `slide(kaynak.jpg, en, tr, cikti.jpg)` / kapak: `cover(...)`. Metin bandını siler, aynı yerleşimle yeniden yazar (Poppins; SemiBold `fonts/` içinde). Görsel `gunluk-ingilizce-carousel` reposuna push edilir, Metricool raw linkten çeker.

## Kaynak klipler
`/mnt/user-data/uploads/` – oturumla birlikte gider, Mehmet yeniden ekler. Kullanım günlüğü: `ortak/takvim.md`.
