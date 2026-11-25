# Cevap: "Uygulama ekibinden içerik talebi: mağaza yorumu" (2026-11-25_uygulama_ekibinden_icerik_talebi_magaza_yorumu.md)

**Kimden:** Adam Koseri ve ekip (Brené Braun, Seth Codin, Mr. Feast, Charlie Hunger) · **Durum:** öneri, Mehmet'in onayını bekliyor

## Karar: reel değil, HİKAYE dizisi
- Reel takipçi dışına gider; o kitle uygulamayı kullanmıyor (sınır 3 ve satış kokusu riski). 22 Kas verisi: uygulama ağırlıklı Tavşan Adası reeli 2.492 erişim, %78,9 geçme. Yorum isteğini reele koymak hem işe yaramaz hem hesabın keşif sinyallerini düşürür.
- Hikaye yalnız takipçilere gider, bağlantı çıkartması taşır, ertesi gün kaybolur: ızgaraya ve reel erişimine etkisi yok.
- Mehmet'in kalıcı kuralı korunur: yüz/ses yok, ilk ağızdan metin.

## Dizi (gün 1, akşam reelinden ~2 saat sonra)
1. **Kare 1, hikâye (Brené):** "8 yıldır bu hesaptayım. 2 yıldır da tek başıma bir uygulama yapıyorum. Geçen hafta mağazaya şu yorum geldi:" + gerçek yorum, kelimesi kelimesine, takma adla (editörden bekleniyor). Yorum yoksa kare 1 şöyle: "Mağazadaki yorumları tek tek okuyorum. Hepsini."
2. **Kare 2, istek (Seth):** "Daily English'i kullanıyorsan bir dakikanı isteyeceğim: ne düşündüğünü mağazaya yaz. İyi ya da kötü, fark etmez; düzeltmem gerekenleri de oradan öğreniyorum." + **App Store bağlantı çıkartması.**
3. **Kare 3:** "Android'de mi kullanıyorsun? Burası:" + **Google Play bağlantı çıkartması.** (Play'de 1.0.4 yayına girmeden kare 3 çıkmaz; o zamana kadar yalnız iOS.)
4. **Gün 2, teşekkür:** gelen yorumlardan biri kelimesi kelimesine, takma adla + "Okudum. Teşekkürler." Kapanış bu; ikinci kez istenmez.
- Kalıcı: hikayeler "Yorumlar" adlı öne çıkanlara eklenir (profilde her zaman açık, maliyetsiz).

## Kanca (Mr. Feast)
Satış değil, itiraf: "8 yıl / 2 yıl / tek başıma". Takipçi Mehmet'i hiç görmedi; perde arkasından tek cümle merak uyandırır. Yıldız, ödül, "destek ol" dili yok.

## Uyum ve risk (Charlie)
- Ödül, çekiliş, Premium yok; "5 yıldız" denmez; "kullanıyorsan" diye başlar (sınır 1–3). ✅
- Uydurma yorum yok; gerçek yorum yoksa kare 1'in yedek metni kullanılır (sınır 5). ✅
- Satış kokusu: dizi 3 karede biter, tek günlük; aynı hafta ikinci kez istenmez. Ertesi gün normal içerik.
- Takipçi kaybı riski düşük: hikayelerden çıkış takipten çıkmak değildir. Ölçeriz: dizi günü takipçi değişimi.

## Takvim
- **Gün:** Play'de 1.0.4 yayına girdiği gün; o güne kadar beklemeyeceksek iOS'la Per 26 akşamı, Play çıkınca tek kare (kare 3) eklenir.
- Izgaraya etkisi: yok.

## Ölçü
- Bağlantı çıkartması tıklamaları ve kare başına görüntülenme (hikaye içgörüsü, Mehmet ekran görüntüsü atar ya da Metricool).
- Mağaza yorum sayısı: önceki gün, +3, +7 (uygulama ekibi).

## Uygulama ekibinden ihtiyaç
- Üç gerçek mağaza yorumunun metni ve takma adları (editör).
- Play 1.0.4 yayın tarihi.

## Uygulama (25 Kas 19:10)
Mehmet onayladı: Per 26 akşamı yalnız iOS ile başlıyor. Kareler: `icerik/2026-11-26_hikaye_magaza-yorumu/`. Yorumlar App Store sayfasından çekildi (7 yorum, Play'de yorum yok). Editörden yorum metni istemeye gerek kalmadı; Play 1.0.4 tarihi hâlâ bekleniyor.

## Son karar (25 Kas 19:35, Mehmet)
Instagram'dan yalnız tek bir hikaye karesi: doğrudan, yorum alıntısız istek + App Store bağlantısı (Per 26 akşam). Android karesi, teşekkür karesi ve dizi yok.
Uygulama ekibine: asıl ve sürekli yol uygulama içi istek. Mehmet "ya direkt iste ya da sadece uygulama içi isteyelim" dedi. Öneri: iOS'ta sistemin yerleşik puanlama penceresi (SKStoreReviewController / Flutter in_app_review), Play'de In-App Review API; olumlu bir anın ardından (ör. okuma bitişi, seri günü) gösterilsin. Kodda var mı önce kontrol edilsin (ekip kuralı); karar ve ölçüm uygulama ekibinde.
