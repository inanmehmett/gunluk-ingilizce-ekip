# Tavşan Adası (The Island Where Rabbits Won) · 21 Kas · reel + hikaye (Mehmet onayı 01:03)
Kaynak: ScreenRecording_11-21-2026 00-20-01 (uygulamanın sesli okuması + dokunuşlar: visitors, food, on purpose=kasten, bilerek (kalıp), 1929'da, poison=zehir, empty=boş).
Ses kesimleri (kayıt saniyesi): For thirty years 43.7–45.6 · It was removed…on purpose 46.75–49.35 · başlık The Island That Was Erased 54.7–56.25 · In 1929…poison gas 62.8–67.2. Hikaye: 7.2–14.0, 15.6–16.9, 22.35–25.35, 37.65–42.35 + son ikisi.
Reel 15,6 sn: hook "Bu ada 30 yıl haritada yoktu." ilk karede tam; on purpose balonu 6.35 sn; poison balonu 13.95 sn; müzik Mehmet/Edits. Hikaye 29 sn: "Bu akşam ne okuyorsun?", visitors + on purpose balonları, altta link çıkartması boşluğu.
Render: HyperFrames (index.html) + ffmpeg ses birleştirme (apad).
v2 (01:15, Mehmet: akıcılık): hikaye sesi cümle cümle değil, kesintisiz bloklarla (kayıt 7.0–17.2, 22.0–25.8, 37.3–49.8), uygulamanın doğal duraklamaları korundu; 32 sn.
v3 (21 Kas 12:05): ses erken başlıyordu. Neden: ffmpeg 6.1 adelay bu kayıtta uygulanmıyordu, bütün ses ~1,8 sn (reelde 1 sn) erkendi. Çözüm: araclar/reels/ses_yerlestir.py ile sesi örnek düzeyinde yerleştirme; hikaye ve reel yeniden birleştirildi, ses ilk vurguyla eşzamanlı.
