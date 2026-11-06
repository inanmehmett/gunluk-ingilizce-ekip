# Kaynak etiketi standardı — spesifikasyon

**Tarih:** 6 Kasım 2026 · **Hazırlayan:** Nate Gümüş + Steve İşler (Daily English), Nate Gold (Instagram) görüşüyle · **Uygulayacak:** Mehmet / editördeki asistan (kod burada yazılmıyor, sadece ihtiyaç ve gerekçe)
**Sebep:** 6 Kas çapraz ekip toplantısında kararlaştırıldı, henüz kurulmadı. Link tıklama → indirme → aktivasyon zincirini ölçmeden pazarlama planının işe yarayıp yaramadığını göremiyoruz (bkz. `raporlar/2026-11-06_pazarlama_stratejisi.md`, madde 1).

## 1. Sorun
Instagram ekibi yalnızca **profil linki tıklamasını** raporluyor (Metricool). Bu tıklamanın kaç gerçek indirmeye, kaç hesap açmaya, kaç aboneliğe dönüştüğü bilinmiyor. İki platform farklı kısıt getiriyor:
- **Android:** Google Play, linke eklenen `referrer` parametresini native olarak destekliyor — ek bir servis gerekmiyor.
- **iOS:** App Store, indirme sonrası uygulamaya kampanya parametresi taşımıyor (Apple Arama Reklamları hariç — organik Instagram trafiği için işe yaramaz). Üçüncü parti bir attribution servisi (Branch/AppsFlyer/Adjust) kurmadan teknik olarak güvenilir bir eşleştirme yok.

## 2. Önerilen çözüm — güncellendi (6 Kas 2026, aynı gün)

**Mehmet'in talimatı: onboarding akışına hiçbir şey eklenmeyecek.** Aşağıdaki "A katmanı" (self-report sorusu) bu yüzden geri çekildi. Geriye yalnızca onboarding'e dokunmayan, native/arka plan mekanizmalar kalıyor:

### Android: Play Install Referrer (tek katman, ekrana dokunmaz)
Google Play, mağaza linkine `&referrer=utm_source%3Dinstagram%26utm_medium%3D<tür>%26utm_content%3D<içerik_id>` eklenmesine izin veriyor; Play Store bunu ilk açılışta uygulamaya native olarak iletiyor (Play Install Referrer API). Instagram ekibi paylaştığı her linke (bio, story, post) bu parametreyi ekler:
- `utm_medium`: `bio` | `story` | `post_reel` | `post_carousel`
- `utm_content`: paylaşılan içeriğin tarihi/kısa kodu (ör. `20261106_lansman`)

**Neden bu:** Hiçbir UI eklemez, native Play Store mekanizması. Yalnızca link formatı ve backend'de bir alanı okuyup kaydetmek yeterli.

### iOS: açık boşluk, çözümsüz kaldı
Apple, indirme sonrası uygulamaya kampanya parametresi taşımıyor (Arama Reklamları hariç, organik Instagram trafiği için işe yaramaz). Onboarding'e soru eklenemeyeceğine göre, iOS'ta **şu an ekstra efor/maliyetsiz bir çözüm yok.** İki seçenek var, ikisi de bu raporun kapsamı dışında bırakıldı: (1) üçüncü parti attribution servisi (Branch/AppsFlyer) — maliyetli, bu ölçekte orantısız; (2) native "rate us"/anket API'si dışında bir native prompt yok. **Sonuç: iOS'ta kaynak ölçümü, Android'deki Play Referrer kadar güvenilir olamayacak — bu bilinen, kabul edilen bir boşluk, çözülmedi.**

## 3. Instagram ekibinin yapması gereken değişiklik
Adam Koseri / Nate Gold: Paylaşılan her link (profil, story, carousel) yukarıdaki `utm_medium`/`utm_content` formatında olmalı. Bu, Instagram ekibinin içerik kararına karışmıyor — yalnızca link formatı standardı.

## 4. Nate Gümüş'ün haftalık rapor değişikliği
Mevcut huni (`ortak/hedef.md`) artık Android için `utm_medium` kırılımıyla raporlanır. iOS tarafında kaynak kırılımı yapılamıyor — iOS indirmeleri "kaynağı bilinmiyor" olarak kalır.

## 5. Kapsam dışı (bilerek)
Üçüncü parti attribution servisi (Branch/AppsFlyer) şimdilik önerilmiyor — bu ölçekte (haftalık onlarca indirme) maliyeti/entegrasyon eforu kazancını geçer. Ölçek büyürse (aylık 1000+ indirme) yeniden değerlendirilir.

## İtirazlar
- **Charlie Hunger (Instagram ekibi):** Instagram ekibine link formatı değişikliği yük bindiriyor — her paylaşımda doğru `utm_medium` girilmesi unutulabilir. **Öneri:** Adam Koseri, `ortak/takvim.md`'ye link şablonunu sabit bir sütun olarak ekler, elle hatırlamaya bırakmaz.
- **Nassim Talip:** iOS'ta hiçbir ölçüm yokken "kaynak etiketi standardı kuruldu" demek yanıltıcı olur — rapor bunun yalnızca Android'i kapsadığını, iOS'un açık kaldığını her yerde açıkça yazmalı. **Kabul edildi.**

## Mehmet'e / editöre giden iş tanımı (özet)
1. Android: Play Install Referrer API'den gelen `referrer` string'i ilk açılışta okunup backend'e gönderilir. (Onboarding'e dokunulmaz.)
2. Backend: bu alan kullanıcı kaydına eklenir; haftalık rapor sorgusu Android için kaynağa göre kırılım döner.
3. Instagram ekibi: paylaştığı linklere `utm_medium`/`utm_content` formatını uygular (yalnızca Android mağaza linkinde anlamlı).
4. iOS kaynak ölçümü: çözülmedi, açık madde olarak kalıyor.
