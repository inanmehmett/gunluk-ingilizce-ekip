# Kaynak etiketi standardı — spesifikasyon

**Tarih:** 6 Kasım 2026 · **Hazırlayan:** Nate Gümüş + Steve İşler (Daily English), Nate Gold (Instagram) görüşüyle · **Uygulayacak:** Mehmet / editördeki asistan (kod burada yazılmıyor, sadece ihtiyaç ve gerekçe)
**Sebep:** 6 Kas çapraz ekip toplantısında kararlaştırıldı, henüz kurulmadı. Link tıklama → indirme → aktivasyon zincirini ölçmeden pazarlama planının işe yarayıp yaramadığını göremiyoruz (bkz. `raporlar/2026-11-06_pazarlama_stratejisi.md`, madde 1).

## 1. Sorun
Instagram ekibi yalnızca **profil linki tıklamasını** raporluyor (Metricool). Bu tıklamanın kaç gerçek indirmeye, kaç hesap açmaya, kaç aboneliğe dönüştüğü bilinmiyor. İki platform farklı kısıt getiriyor:
- **Android:** Google Play, linke eklenen `referrer` parametresini native olarak destekliyor — ek bir servis gerekmiyor.
- **iOS:** App Store, indirme sonrası uygulamaya kampanya parametresi taşımıyor (Apple Arama Reklamları hariç — organik Instagram trafiği için işe yaramaz). Üçüncü parti bir attribution servisi (Branch/AppsFlyer/Adjust) kurmadan teknik olarak güvenilir bir eşleştirme yok.

## 2. Önerilen çözüm — iki katmanlı, düşük maliyetli

### A) Birincil katman (her iki platform, self-report): Onboarding'de "Bizi nereden duydun?"
Hesap açma/ilk kullanım akışına tek bir soru eklenir:
> "Daily English'i nereden duydun?" — seçenekler: **Instagram (@gunluk_ingilizce)** · Arkadaş tavsiyesi · App Store/Play Store arama · Diğer

**Neden bu:** Üçüncü parti attribution servisi kurmadan (maliyet + entegrasyon işi) her iki platformda da çalışan tek standart bu. Kesin değil ama yeterli sinyal — kullanıcı kendi hatırladığını söylüyor.
**Kabul kriteri:** Cevap backend'de kullanıcı kaydına bir alan olarak tutulur (`acquisition_source`), Nate Gümüş'ün haftalık raporunda "kaynağa göre indirme/aktivasyon/abonelik" kırılımı olarak görünür.

### B) İkincil katman (yalnızca Android, doğrulama amaçlı): Play Install Referrer
Google Play, mağaza linkine `&referrer=utm_source%3Dinstagram%26utm_medium%3D<tür>%26utm_content%3D<içerik_id>` eklenmesine izin veriyor; Play Store bunu ilk açılışta uygulamaya native olarak iletiyor (Play Install Referrer API). Instagram ekibi paylaştığı her linke (bio, story, post) bu parametreyi ekler:
- `utm_medium`: `bio` | `story` | `post_reel` | `post_carousel`
- `utm_content`: paylaşılan içeriğin tarihi/kısa kodu (ör. `20261106_lansman`)

**Neden bu:** Android'de A katmanının (self-report) doğruluğunu çapraz kontrol eder — "Instagram dedi" diyen kullanıcı oranı ile gerçek referrer verisi karşılaştırılır. Ek bir servis/SDK gerekmez, yalnızca link formatı ve backend'de bir alanı okuyup kaydetmek yeterli.
**iOS'ta bu katman yok** — Apple böyle bir mekanizma sunmuyor; A katmanı iOS'ta tek kaynak olarak kalır.

## 3. Instagram ekibinin yapması gereken değişiklik
Adam Koseri / Nate Gold: Paylaşılan her link (profil, story, carousel) yukarıdaki `utm_medium`/`utm_content` formatında olmalı. Bu, Instagram ekibinin içerik kararına karışmıyor — yalnızca link formatı standardı.

## 4. Nate Gümüş'ün haftalık rapor değişikliği
Mevcut huni (`ortak/hedef.md`) artık şu kırılımla raporlanır: her huni adımı (indirme, aktivasyon, abonelik) kaynağa göre (`Instagram` / `Diğer` / Android için ek olarak `utm_medium` kırılımı) ayrılır. Bu, pazarlama stratejisinin işe yarayıp yaramadığının **tek doğrulama yolu**.

## 5. Kapsam dışı (bilerek)
Üçüncü parti attribution servisi (Branch/AppsFlyer) şimdilik önerilmiyor — bu ölçekte (haftalık onlarca indirme) maliyeti/entegrasyon eforu kazancını geçer. Ölçek büyürse (aylık 1000+ indirme) yeniden değerlendirilir.

## İtirazlar
- **Nassim Talip:** Self-report (A katmanı) hafızaya dayanıyor, kullanıcı yanlış hatırlayabilir veya "Diğer"i seçebilir — bu "kesin veri" değil, "en iyi elimizdeki sinyal". Rapor bunu "Ders" değil her zaman "gözlem" olarak sunmalı, küçük örneklemde özellikle. **Kabul edildi**, madde 2'deki "kabul kriteri" buna göre yazıldı — kırılım raporlanır ama kesinlik iddia edilmez.
- **Charlie Hunger (Instagram ekibi):** Instagram ekibine link formatı değişikliği yük bindiriyor — her paylaşımda doğru `utm_medium` girilmesi unutulabilir. **Öneri:** Adam Koseri, `ortak/takvim.md`'ye link şablonunu sabit bir sütun olarak ekler, elle hatırlamaya bırakmaz.

## Mehmet'e / editöre giden iş tanımı (özet)
1. Onboarding'e tek soruluk "nereden duydun" ekranı — cevap `acquisition_source` alanında saklanır.
2. Android: Play Install Referrer API'den gelen `referrer` string'i ilk açılışta okunup backend'e gönderilir.
3. Backend: kullanıcı kaydına bu iki alan eklenir; haftalık rapor sorgusu kaynağa göre kırılım döner.
4. Instagram ekibi: paylaştığı linklere `utm_medium`/`utm_content` formatını uygular (yalnızca Android mağaza linkinde anlamlı; iOS linkinde formatın bir etkisi yok ama tutarlılık için aynı şekilde yazılabilir).
