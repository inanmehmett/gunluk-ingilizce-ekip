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

## reels/ladder.py
Seviye merdiveni overlay'i (A1→B2 şeridi + emoji'li hook).
`python3 ladder.py <basamak> <klip> <baslangic> <sure> cikti.mp4`

## carousel/build.py + data.py
`data.py` tüm set metinlerini tutar (tek doğru kaynak). `build_sel.py KOD KOD` sadece seçilen setleri yeniden üretir.
Görseller `gunluk-ingilizce-carousel` (public) reposuna kopyalanır; Metricool raw.githubusercontent.com linkiyle çeker.

## Kaynak klipler
`/mnt/user-data/uploads/` – oturumla birlikte gider, Mehmet yeniden ekler. Kullanım günlüğü: `ortak/takvim.md`.
