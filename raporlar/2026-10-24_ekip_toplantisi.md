# Ekip toplantısı – ilk üretimin değerlendirmesi (24 Eki 2026)

Konu: Seviye testi 1/6 · A1 reeli. Kaynaklar: `reels/seviye/` (taslak, spec_a1.json, açıklama), README, el kitapları.

## Katılımcılar
Adam Koseri (yönetti), Sal Kaan, Mr. Feast, David Kristal, Tomris Uyan, Jony Ayv, Walter Marş, Daniel Kahraman, Gary Bee, Nate Gold, Seth Codin, Brené Braun, Reid Hoffmann, Charlie Hunger.

## Ne oldu / kök nedenler
Bu üretimde Mehmet 7 hata yakaladı. Sal'ın el kitabındaki 4 "Mehmet yakaladı" dersiyle toplam 11 oldu.

1. **Hook anketi:** Anketler inceleme akışının dışındaydı. *Kök neden: içerik sayılmayan parçaların sahibi yok.*
2. **Çay:** Tomris kalıp yerine fiile itiraz etti, ardından "doldurmak"ı önerdi. David kendi alternatifini denemedi. *Kök neden: itiraz kontrol edilmeden yazıldı, iki uzman birbirine yaslandı.*
3. **İtiraz edenin onayı yok:** Dosyalar hâlâ uyuşmuyor. Hook taslakta "bir sonraki seviyeye geç", spec ve açıklamada "A1'i geçtin". Çay cümlesi taslakta "yaparım", açıklamada "hazırlarım", Tomris'in el kitabında "kendime… koyarım". Onay satırı yok. *Kök neden: tek doğru dosya yok.*
4. **David ile Tomris:** "Türkçesi" bölümünün işlevi hiçbir yerde tanımlı değildi. Kural 10 ile çözüldü. El kitabındaki "kendime" bu kurala aykırı; kurala uyan, açıklamadaki sürüm.
5. **"A1'i geçtin":** Sal bunu "isteğe bağlı" diye işaretledi. David'in "seviye yaklaşık verilir" kuralı devreye girmedi. Daniel kadroda değildi. Yorumlarımızdaki "Okuma B2, dinleme A2, konuşma A1" cümlesi tek bir okuma metninin seviye belirlemediğini gösteriyor. *Kök neden: dürüstlük için engel etiketi yok, kadro eksik kuruldu.*
6. **"Seviye testi" adı:** Aynı abartı seri adında da vardı; adı ayrıca kimse incelemedi.
7. **"A1"in "Al" gibi okunması:** Bunu Jony değil Sal yakaladı. *Kök neden: harf ve rakam kontrolü yok.*
8. **Merdiven anlatılmadı:** Ekranda "1/6" var ama A1'den B2'ye 6 basamak olduğu söylenmiyor. *Kök neden: seri kurgusu iç dosyada kaldı.*

Adam: "El kitaplarında ekipte olmayan kişilere atıf var (Sam, Mia, Nora). Sahiplik dağınık."
Charlie: "Bu kuralların hepsi hipotez. Ölçüsü de Mehmet'in yakaladığı hata sayısı."

## Kararlar
1. **Tek paket dosyası:** Hook, ekran metni, Türkçesi, açıklama ve spec tek `PAKET.md` dosyasından türetilir. Render'dan önce mp4, spec ve açıklama paketle satır satır karşılaştırılır. — *Sal, Walter*
2. **Onay satırı zorunlu:** Satır sürüm numarasıyla yazılır (ör. "v3 · David ✅ · Tomris ✅ · Jony ✅ · Sal ✅"). İtiraz eden üye son sürümü kendisi onaylar. Onay satırı olmayan paket gönderilmez. — *Sal*
3. **ENGEL / DÜZELT / ÖNERİ etiketleri:** Dürüstlük, seviye iddiası, kanıtsız iddia ve kural 8 ya da 10 ihlali her zaman ENGEL'dir; "isteğe bağlı" sayılamaz. Açık ENGEL varken son kapı geçilmez. — *Sal, herkes*
4. **Kadro:** Yeni seri, format ya da hook için Mr. Feast, Daniel, David ve Charlie zorunlu. — *Sal*
5. **Seviye dili:** İzleyicinin değil, metnin seviyesi söylenir; "geçtin" yok. Seviye Oxford listelerine göre "yaklaşık" diye verilir. — *David, Daniel*
6. **Seri yeniden adlandırılıyor:** "Seviye testi" adı bırakılıyor. Mr. Feast, Tomris ve Daniel 27 Ekim'e kadar 2 ad ve hook önerecek; David ve Sal onaylayacak. Her bölümde ekranda ve açıklamanın ilk satırında "6 basamak: A1 → A2 → A2+ → B1 → B1+ → B2" yazacak. Takvim güncellenecek. — *Mr. Feast, Adam*
7. **Görsel kontrol:** Telefon boyutunda yakın çekimle 1/l/I, 0/O ve A1/Al kontrol edilir. Süre farkı (taslakta ~9 sn, videoda 10 sn) kayda geçirilir. — *Jony, Walter*
8. **Takipçiye giden her soru** (anket, hikâye, yorum) inceleme akışına girer ve kural 8'e göre kontrol edilir. — *Brené, Sal*
9. **Cevap anahtarı:** David, İngilizcedeki her öğenin karşılığı olduğunu ve fazladan bir şey eklenmediğini kontrol eder. Tomris itirazdan önce kontrol listesini uygular. — *David, Tomris*
10. **"Mehmet ne yakalardı?" turu:** Paket gönderilmeden önce 11 hatalık listeyle kontrol edilir. Mehmet'in yakaladığı hatalar paket başına sayılır ve aylık sağlık kontrolünde raporlanır. Hedef sıfır. — *Charlie, Adam*
11. **Mehmet'e çıkış:** Yalnızca şu durumlarda Mehmet'e gidilir: 2 turda çözülmeyen itiraz, üretim veya yeniden render onayı (kural 4), para ve iş birliği mesajları, silme, Mehmet'in sesi ya da zamanı gereken işler. Diğer içerik kararlarını ekip verir. — *Adam*
12. **El kitabı temizliği:** Hayalet atıflar temizlenir, Tomris'in çay kaydı kural 10'a uydurulur, yeni dersler "Hipotez (1 veri noktası)" olarak yazılır. — *Her üye, takip Adam*

## Kişisel taahhütler
- **Adam:** Mehmet'in yakaladığı hata sayısını sağlık kontrolünün ilk satırına yazacağım.
- **Sal:** Dürüstlük sorununa bir daha "isteğe bağlı" demeyeceğim: ya ENGEL ya onay.
- **Mr. Feast:** Her hook'un yanına "bu iddiayı ne kanıtlıyor?" diye yazacağım.
- **David:** Kabul ettiğim her itirazda kendi alternatifimi de bağlam içinde deneyeceğim.
- **Tomris:** İtirazdan önce kontrol listemi uygulayacağım, itirazı yalnızca sorunlu parçaya yazacağım.
- **Jony:** Her render'da benzer görünen harf ve rakamları yakın çekimde kontrol edeceğim.
- **Walter:** Render'dan önce paket, spec ve açıklamayı satır satır eşleştireceğim.
- **Daniel:** Her seride "hak edilmemiş bir başarı ya da başarısızlık duygusu var mı?" diye soracağım.
- **Gary:** Önerdiğim trendleri kural 8'e göre kontrol edeceğim.
- **Nate:** Yeni adın etkisini erişim ve 3 sn+ oranıyla ölçüp sonucu hipotez olarak yazacağım.
- **Seth:** A1 yorumlarında "seviyemi öğrendim" yanılgısı olup olmadığını raporlayacağım.
- **Brené:** Her anketi yayından önce incelemeye sokacağım.
- **Reid:** İş birliği metinlerine de onay satırı ve ENGEL kuralını uygulayacağım.
- **Charlie:** Hiçbir paketi "Mehmet ne yakalardı?" turu yapılmadan göndermeyeceğim.

## Mehmet'e sorular
1. "Sayfayı teslim ettim" demen, içerik kararlarında ekibin onay satırının yeterli olduğu, senin yalnızca üretim onayı verdiğin anlamına mı geliyor? A1 videosunu yeni ad ve hook'la yeniden render etmemize onay veriyor musun?
2. Özette çözülen ENGEL'leri de görmek istiyor musun, yoksa yalnızca çözülemeyenleri mi?
3. 24 Ekim hikâye anketinin sonucunu paylaşır mısın? Serinin hangi seviyeden başlayacağına veriyle karar vermek istiyoruz.

İtirazlar: Charlie, "hedef sıfır"ın ilk ay için gerçekçi olmadığını söyledi. İtiraz kayda geçti, karar korundu.
