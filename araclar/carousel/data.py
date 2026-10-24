# -*- coding: utf-8 -*-
# Her set: (seri, kapak satırları, vurgulanan satır, açıklama sorusu, [(en, tr) x8])
K, D, P, H, T = 'Kalıp ifadeler', 'Bunu deme, bunu de', 'Phrasal verb', 'Sık hatalar', 'Temalı kelimeler'

def deme(x): return ('“%s”\ndemeyi bırak,\nbunları kullan' % x, '“%s”' % x)
def pv(v): return ('%s ile\n8 phrasal verb' % v, '%s ile' % v)
def hata(items): return [(a, '“%s” değil' % b) for a, b in items]

SETS = {
# ---------------- KALIP İFADELER ----------------
'K01': (K, 'Her gün\nkullanacağın\n8 İngilizce ifade', '8 İngilizce ifade', 'Bu hafta hangisini kullanacaksın?', [
 ('My bad.', 'Benim hatam.'), ('I’m in.', 'Ben varım.'), ('Fair enough.', 'Mantıklı, tamam.'), ('Hang on.', 'Bir saniye.'),
 ('It’s up to you.', 'Sana kalmış.'), ('I’m starving.', 'Açlıktan ölüyorum.'), ('Never mind.', 'Boş ver.'), ('Sounds good.', 'Olur, güzel.')]),
'K02': (K, 'Dizilerde\nsürekli duyduğun\n8 ifade', '8 ifade', 'En son hangisini bir dizide duydun?', [
 ('You bet.', 'Kesinlikle.'), ('No way!', 'Hadi canım!'), ('I mean it.', 'Ciddiyim.'), ('Got it.', 'Anladım.'),
 ('Hold on.', 'Bekle.'), ('My treat.', 'Ben ısmarlıyorum.'), ('Good call.', 'İyi karar.'), ('For real?', 'Cidden mi?')]),
'K03': (K, 'Arkadaşınla\nkonuşurken\n8 ifade', '8 ifade', 'Bunu en çok kime söylersin? Etiketle.', [
 ('What’s up?', 'Naber?'), ('Long time no see.', 'Uzun zaman oldu.'), ('Catch you later.', 'Sonra görüşürüz.'), ('Take care.', 'Kendine iyi bak.'),
 ('I’m down.', 'Varım.'), ('Count me in.', 'Beni de say.'), ('Keep in touch.', 'Haberleşelim.'), ('Same here.', 'Ben de öyle.')]),
'K04': (K, 'Şaşırınca\nsöylenen\n8 ifade', '8 ifade', 'Seni en son ne bu kadar şaşırttı?', [
 ('You’re kidding!', 'Şaka yapıyorsun!'), ('Are you serious?', 'Ciddi misin?'), ('I can’t believe it.', 'İnanamıyorum.'), ('Unbelievable!', 'İnanılmaz!'),
 ('Wow, really?', 'Vay, gerçekten mi?'), ('That’s insane.', 'Bu çılgınca.'), ('Oh my God!', 'Aman Tanrım!'), ('I’m shocked.', 'Şok oldum.')]),
'K05': (K, 'Bir şey\nrica ederken\n8 ifade', '8 ifade', 'En çok hangisi işine yarar?', [
 ('Do me a favor.', 'Bana bir iyilik yap.'), ('Give me a hand.', 'Bana yardım et.'), ('Could you help me?', 'Yardım eder misin?'), ('Quick question.', 'Kısa bir sorum var.'),
 ('Got a minute?', 'Bir dakikan var mı?'), ('Say that again?', 'Bir daha söyler misin?'), ('Whenever you can.', 'Müsait olduğunda.'), ('Thanks in advance.', 'Şimdiden teşekkürler.')]),
'K06': (K, 'Yorulunca\nve bıkınca\n8 ifade', '8 ifade', 'Bugün hangisi tam senlik?', [
 ('I’m exhausted.', 'Bitkinim.'), ('I’m done with this.', 'Bu iş bende bitti.'), ('I can’t take it anymore.', 'Artık dayanamıyorum.'), ('I need a break.', 'Bir molaya ihtiyacım var.'),
 ('I’m fed up.', 'Bıktım.'), ('Give me a break.', 'Hadi ama! / Bir rahat bırak.'), ('I’m worn out.', 'Çok yoruldum.'), ('Leave me alone.', 'Beni yalnız bırak.')]),
'K07': (K, 'Sevinince\nsöylenen\n8 ifade', '8 ifade', 'Seni en son ne böyle sevindirdi?', [
 ('I’m so happy.', 'Çok mutluyum.'), ('I made it!', 'Başardım!'), ('This is great!', 'Bu harika!'), ('I can’t wait.', 'Sabırsızlanıyorum.'),
 ('Best day ever.', 'Hayatımın en güzel günü.'), ('I’m thrilled.', 'Havalara uçuyorum!'), ('Finally!', 'Sonunda!'), ('Lucky me!', 'Ne şanslıyım!')]),
'K08': (K, 'Biri üzgünken\nsöylenecek\n8 ifade', '8 ifade', 'Bugün bunu duymaya ihtiyacı olan birine gönder.', [
 ('I’m here for you.', 'Yanındayım.'), ('It’s okay.', 'Sorun yok.'), ('Take your time.', 'Acele etme.'), ('It happens.', 'Olur böyle şeyler.'),
 ('Hang in there.', 'Dayan, pes etme.'), ('You’ll be fine.', 'İyi olacaksın.'), ('Cheer up.', 'Neşelen.'), ('It’s not your fault.', 'Senin suçun değil.')]),
'K09': (K, 'Katılırken ve\nkatılmazken\n8 ifade', '8 ifade', 'Sen en çok hangisini kullanıyorsun?', [
 ('Exactly.', 'Aynen öyle.'), ('I agree.', 'Katılıyorum.'), ('You’re right.', 'Haklısın.'), ('I don’t think so.', 'Sanmıyorum.'),
 ('Not really.', 'Pek sayılmaz.'), ('I see your point.', 'Demek istediğini anladım.'), ('Totally.', 'Kesinlikle.'), ('No doubt.', 'Şüphesiz.')]),
'K10': (K, 'Acelen\nvarken\n8 ifade', '8 ifade', 'Hep geç kalan arkadaşına gönder.', [
 ('I’m in a hurry.', 'Acelem var.'), ('Hurry up.', 'Acele et.'), ('I’m running late.', 'Geç kalıyorum.'), ('I’ve got to go.', 'Gitmem lazım.'),
 ('Make it quick.', 'Çabuk ol.'), ('I don’t have time.', 'Vaktim yok.'), ('I’m on my way.', 'Yoldayım.'), ('Be right back.', 'Hemen dönüyorum.')]),
'K11': (K, 'Emin\nolmadığında\n8 ifade', '8 ifade', 'Kararsız kaldığında hangisini söylersin?', [
 ('Maybe.', 'Belki.'), ('I guess so.', 'Sanırım öyle.'), ('We’ll see.', 'Bakarız.'), ('Kind of.', 'Biraz, sayılır.'),
 ('Could be.', 'Olabilir.'), ('I doubt it.', 'Sanmam.'), ('Hard to say.', 'Söylemesi zor.'), ('Let me think.', 'Bir düşüneyim.')]),
'K12': (K, 'Telefonda\nişine yarayacak\n8 ifade', '8 ifade', 'Telefonda İngilizce konuşmak seni de geriyor mu?', [
 ('Who’s calling?', 'Kim arıyor?'), ('Can you hear me?', 'Beni duyuyor musun?'), ('You’re breaking up.', 'Sesin kesiliyor.'), ('I’ll call you back.', 'Seni sonra ararım.'),
 ('Hold on, please.', 'Hatta kalın lütfen.'), ('Sorry, wrong number.', 'Pardon, yanlış numara.'), ('Speak up, please.', 'Biraz yüksek sesle lütfen.'), ('Text me.', 'Bana mesaj at.')]),
'K13': (K, 'Yemek\nmasasında\n8 ifade', '8 ifade', 'Sofrada en çok hangisini söylersin?', [
 ('I’m full.', 'Doydum.'), ('It’s delicious.', 'Çok lezzetli.'), ('Help yourself.', 'Buyur, al.'), ('Enjoy!', 'Afiyet olsun.'),
 ('Some more, please.', 'Biraz daha lütfen.'), ('Pass the salt.', 'Tuzu uzat.'), ('It smells great.', 'Harika kokuyor.'), ('Dig in.', 'Hadi, yemeye başla.')]),
'K14': (K, 'Bir şeyi\nunutunca\n8 ifade', '8 ifade', 'En son neyi unuttun?', [
 ('I forgot.', 'Unuttum.'), ('It slipped my mind.', 'Aklımdan çıkmış.'), ('I can’t remember.', 'Hatırlayamıyorum.'), ('Remind me.', 'Bana hatırlat.'),
 ('That reminds me.', 'Aklıma gelmişken.'), ('That rings a bell.', 'Tanıdık geliyor.'), ('Now I remember.', 'Şimdi hatırladım.'), ('My mind went blank.', 'Kafam durdu.')]),
'K15': (K, 'İşte her gün\nduyacağın\n8 ifade', '8 ifade', 'İş arkadaşına gönder, o anlar.', [
 ('Let’s get started.', 'Başlayalım.'), ('I’ll handle it.', 'Ben hallederim.'), ('Keep me posted.', 'Beni haberdar et.'), ('Any updates?', 'Gelişme var mı?'),
 ('Let’s wrap up.', 'Toparlayalım.'), ('I’m swamped.', 'İşten başımı kaldıramıyorum.'), ('Well done.', 'Tebrikler, harika iş.'), ('Sounds like a plan.', 'Güzel plan.')]),
'K16': (K, 'Plan\nyaparken\n8 ifade', '8 ifade', 'Bu hafta kiminle plan yapıyorsun?', [
 ('Are you free?', 'Müsait misin?'), ('Let’s meet up.', 'Buluşalım.'), ('What time?', 'Saat kaçta?'), ('Works for me.', 'Bana uyar.'),
 ('I can’t make it.', 'Gelemiyorum.'), ('Maybe next time.', 'Belki başka zaman.'), ('See you there.', 'Orada görüşürüz.'), ('It’s a deal.', 'Anlaştık.')]),
'K17': (K, 'Sinirlenince\nsöylenen\n8 ifade', '8 ifade', 'Seni en çok ne sinirlendirir?', [
 ('Enough!', 'Yeter!'), ('Cut it out.', 'Kes şunu.'), ('I’m sick of it.', 'Bundan bıktım.'), ('Are you kidding me?', 'Dalga mı geçiyorsun?'),
 ('That’s not fair.', 'Bu haksızlık.'), ('Back off.', 'Geri çekil.'), ('Whatever.', 'Her neyse.'), ('Don’t push me.', 'Üstüme gelme.')]),
'K18': (K, 'Teşekkür ve\niltifat için\n8 ifade', '8 ifade', 'Bugün bunu hak eden birine gönder.', [
 ('I appreciate it.', 'Gerçekten teşekkür ederim.'), ('You made my day.', 'Günümü güzelleştirdin.'), ('That’s so kind of you.', 'Çok naziksin.'), ('I owe you one.', 'Sana borçlandım.'),
 ('You’re the best.', 'Harikasın.'), ('Good for you.', 'Ne güzel, sevindim.'), ('Nice job.', 'Güzel iş.'), ('You look great.', 'Harika görünüyorsun.')]),
'K19': (K, 'Vedalaşırken\nkullanacağın\n8 ifade', '8 ifade', '“Bye” dışında hangisini kullanıyorsun?', [
 ('See you soon.', 'Yakında görüşürüz.'), ('Have a good one.', 'İyi günler.'), ('Good night.', 'İyi geceler.'), ('Sleep tight.', 'İyi uykular.'),
 ('Safe travels.', 'İyi yolculuklar.'), ('Say hi to your mom.', 'Annene selam söyle.'), ('See you later.', 'Sonra görüşürüz.'), ('Get home safe.', 'Eve sağ salim git.')]),
# ---------------- BUNU DEME, BUNU DE ----------------
'D01': (D, *deme('I don’t know'), 'Hep “I don’t know” diyen arkadaşına gönder.', [
 ('I have no idea.', 'Hiçbir fikrim yok.'), ('Beats me.', 'Bilmem ki.'), ('No clue.', 'En ufak fikrim yok.'), ('Who knows?', 'Kim bilir?'),
 ('I can’t tell.', 'Kestiremiyorum.'), ('Don’t ask me.', 'Bana sorma.'), ('Not that I know of.', 'Bildiğim kadarıyla hayır.'), ('I’ll find out.', 'Öğrenir, söylerim.')]),
'D02': (D, *deme('Very good'), 'Sen en çok hangisini kullanıyorsun?', [
 ('Awesome.', 'Harika.'), ('Amazing.', 'Müthiş.'), ('Excellent.', 'Mükemmel.'), ('Brilliant.', 'Süper.'),
 ('Fantastic.', 'Şahane.'), ('Impressive.', 'Etkileyici.'), ('Outstanding.', 'Olağanüstü.'), ('Not bad at all.', 'Hiç fena değil.')]),
'D03': (D, *deme('Thank you'), 'Teşekkür borcun olan birine gönder.', [
 ('Thanks a lot.', 'Çok teşekkürler.'), ('Thanks a million.', 'Çok çok teşekkürler!'), ('Thanks for everything.', 'Her şey için teşekkürler.'), ('Thanks a ton.', 'Çok ama çok sağ ol.'),
 ('You’re a lifesaver.', 'Hayat kurtardın.'), ('Cheers.', 'Sağ ol.'), ('Much appreciated.', 'Çok makbule geçti.'), ('That means a lot.', 'Benim için çok değerli.')]),
'D04': (D, *deme('You’re welcome'), 'Hangisini ilk kez duydun?', [
 ('No problem.', 'Sorun değil.'), ('My pleasure.', 'Benim için zevkti.'), ('Anytime.', 'Her zaman.'), ('Don’t mention it.', 'Rica ederim.'),
 ('No big deal.', 'Hiç sorun değil.'), ('Happy to help.', 'Memnuniyetle.'), ('It’s nothing.', 'Bir şey değil.'), ('No worries.', 'Önemli değil.')]),
'D05': (D, *deme('I’m sorry'), 'En son kimden özür diledin?', [
 ('I apologize.', 'Özür dilerim.'), ('Sorry about that.', 'Kusura bakma.'), ('It was my fault.', 'Benim suçumdu.'), ('I’m so sorry.', 'Çok özür dilerim.'),
 ('I didn’t mean to.', 'İsteyerek yapmadım.'), ('Sorry, my mistake.', 'Pardon, benim hatam.'), ('I feel terrible.', 'Çok kötü hissediyorum.'), ('It won’t happen again.', 'Bir daha olmayacak.')]),
'D06': (D, *deme('I’m tired'), 'Bugün hangisisin?', [
 ('I’m beat.', 'Çok yorgunum.'), ('I’m drained.', 'Tükendim.'), ('I’m wiped out.', 'Bitkin düştüm.'), ('I’m sleepy.', 'Uykum var.'),
 ('I’m dead tired.', 'Yorgunluktan ölüyorum.'), ('I’m running on empty.', 'Enerjim kalmadı.'), ('I need some rest.', 'Dinlenmem lazım.'), ('I can barely stand.', 'Ayakta zor duruyorum.')]),
'D07': (D, *deme('Yes'), 'Sen “yes” yerine ne diyorsun?', [
 ('Sure.', 'Tabii.'), ('Of course.', 'Elbette.'), ('Absolutely.', 'Kesinlikle.'), ('Definitely.', 'Hiç şüphesiz.'),
 ('Why not?', 'Neden olmasın?'), ('Sure thing.', 'Tabii ki.'), ('I’d love to.', 'Çok isterim.'), ('Yeah, sure.', 'Evet, tabii.')]),
'D08': (D, *deme('No'), 'Hayır demekte zorlanan birine gönder.', [
 ('Not now.', 'Şimdi olmaz.'), ('No, thanks.', 'Yok, sağ ol.'), ('I’m afraid not.', 'Maalesef hayır.'), ('Not a chance.', 'Asla olmaz.'),
 ('I’d rather not.', 'Yapmasam daha iyi.'), ('Nope.', 'Yok.'), ('Not today.', 'Bugün olmaz.'), ('I’ll pass.', 'Ben almayayım.')]),
'D09': (D, *deme('I like it'), 'Senin “I can’t get enough” dediğin şey ne?', [
 ('I love it.', 'Bayıldım.'), ('I’m into it.', 'İlgimi çekiyor.'), ('I’m a big fan.', 'Büyük hayranıyım.'), ('It’s my thing.', 'Tam bana göre.'),
 ('I’m crazy about it.', 'Buna bayılıyorum.'), ('I enjoy it.', 'Keyif alıyorum.'), ('It’s my favorite.', 'En sevdiğim bu.'), ('I can’t get enough.', 'Doyamıyorum.')]),
'D10': (D, *deme('How are you?'), 'Uzun zamandır yazmadığın birine gönder.', [
 ('How’s it going?', 'Nasıl gidiyor?'), ('How have you been?', 'Görüşmeyeli nasılsın?'), ('What’s new?', 'Ne var ne yok?'), ('How’s everything?', 'Her şey nasıl?'),
 ('How are things?', 'İşler nasıl?'), ('You alright?', 'İyi misin?'), ('How’s your day going?', 'Günün nasıl geçiyor?'), ('What’s going on?', 'Neler oluyor?')]),
# ---------------- PHRASAL VERB ----------------
'P01': (P, *pv('GET'), 'GET ile bildiğin başka hangisi var?', [
 ('get up', 'kalkmak'), ('get in', '(arabaya) binmek'), ('get out', 'çıkmak'), ('get along', 'iyi geçinmek'),
 ('get over', 'atlatmak'), ('get back', 'geri dönmek'), ('get away', 'kaçmak, uzaklaşmak'), ('get by', 'idare etmek')]),
'P02': (P, *pv('TAKE'), 'TAKE ile bildiğin başka hangisi var?', [
 ('take off', 'kalkış yapmak'), ('take out', 'dışarı çıkarmak'), ('take over', 'devralmak'), ('take up', '(hobiye) başlamak'),
 ('take back', 'geri almak'), ('take after', '(birine) çekmek'), ('take on', 'üstlenmek'), ('take away', 'alıp götürmek')]),
'P03': (P, *pv('PUT'), 'PUT ile bildiğin başka hangisi var?', [
 ('put on', 'giymek'), ('put off', 'ertelemek'), ('put away', 'yerine koymak'), ('put out', 'söndürmek'),
 ('put up with', 'katlanmak'), ('put down', 'yere bırakmak'), ('put together', 'birleştirmek'), ('put back', 'geri koymak')]),
'P04': (P, *pv('GO'), 'GO ile bildiğin başka hangisi var?', [
 ('go on', 'devam etmek'), ('go out', 'dışarı çıkmak'), ('go back', 'geri dönmek'), ('go away', 'gitmek, uzaklaşmak'),
 ('go through', '(zor bir şey) yaşamak'), ('go over', 'gözden geçirmek'), ('go off', '(alarm) çalmak'), ('go ahead', 'buyur, devam et')]),
'P05': (P, *pv('LOOK'), 'LOOK ile bildiğin başka hangisi var?', [
 ('look for', 'aramak'), ('look after', 'bakmak, ilgilenmek'), ('look up', '(sözlükten) bakmak'), ('look forward to', 'dört gözle beklemek'),
 ('look out', 'dikkat etmek'), ('look into', 'araştırmak'), ('look back', 'geriye bakmak'), ('look like', 'benzemek')]),
'P06': (P, *pv('COME'), 'COME ile bildiğin başka hangisi var?', [
 ('come in', 'içeri girmek'), ('come back', 'geri gelmek'), ('come on', 'hadi'), ('come over', 'uğramak'),
 ('come up with', '(fikir) bulmak'), ('come across', 'rastlamak'), ('come out', 'çıkmak, yayınlanmak'), ('come along', 'birlikte gelmek')]),
'P07': (P, *pv('TURN'), 'TURN ile bildiğin başka hangisi var?', [
 ('turn on', 'açmak'), ('turn off', 'kapatmak'), ('turn up', 'sesini açmak'), ('turn down', 'reddetmek'),
 ('turn around', 'arkasını dönmek'), ('turn into', 'dönüşmek'), ('turn out', 'ortaya çıkmak'), ('turn over', 'ters çevirmek')]),
'P08': (P, 'Her gün\nduyacağın\n8 phrasal verb', '8 phrasal verb', 'Bu hafta hangisini kullanacaksın?', [
 ('find out', 'öğrenmek'), ('figure out', 'çözmek, anlamak'), ('pick up', 'almak, kaldırmak'), ('give up', 'vazgeçmek'),
 ('show up', 'çıkıp gelmek'), ('work out', 'spor yapmak'), ('check out', 'göz atmak'), ('end up', 'sonunda … olmak')]),
'P09': (P, *pv('RUN'), 'RUN ile bildiğin başka hangisi var?', [
 ('run away', 'kaçmak'), ('run into', 'karşılaşmak'), ('run out of', 'tükenmek, bitmek'), ('run over', '(arabayla) ezmek'),
 ('run after', 'peşinden koşmak'), ('run through', 'hızlıca gözden geçirmek'), ('run around', 'koşturup durmak'), ('run off', 'kaçıp gitmek')]),
'P10': (P, 'Günlük hayatta\n8 phrasal verb', '8 phrasal verb', 'Hangisini zaten kullanıyordun?', [
 ('hang out', 'takılmak'), ('calm down', 'sakinleşmek'), ('grow up', 'büyümek'), ('wake up', 'uyanmak'),
 ('set up', 'kurmak'), ('fill out', '(form) doldurmak'), ('drop off', '(birini) bırakmak'), ('sign up', 'kaydolmak')]),
# ---------------- SIK HATALAR ----------------
'H01': (H, 'En sık\nyapılan\n8 İngilizce hata', '8 İngilizce hata', 'Dürüst ol: hangisini yapıyordun?', hata([
 ('I agree with you.', 'I am agree'), ('I’m bored.', 'I’m boring'), ('It depends on you.', 'Depends to you'), ('I’m married to her.', 'Married with her'),
 ('Listen to me.', 'Listen me'), ('I went home.', 'I went to home'), ('Call me.', 'Call to me'), ('I really like it.', 'I very like it')])),
'H02': (H, 'Konuşurken\ndilin kaydığı\n8 hata', '8 hata', 'Kaç tanesini doğru biliyordun?', hata([
 ('People are nice.', 'People is'), ('I didn’t go.', 'I didn’t went'), ('She has a car.', 'She have'), ('I’m good at math.', 'Good in math'),
 ('Let’s discuss it.', 'Discuss about it'), ('I enjoy reading.', 'I enjoy to read'), ('Explain it to me.', 'Explain me'), ('Thanks for coming.', 'Thanks for come')])),
'H03': (H, 'Kelime seçiminde\nyapılan\n8 hata', '8 hata', 'En çok hangisini karıştırıyorsun?', hata([
 ('Tell me.', 'Say me'), ('I had fun.', 'I had funny'), ('Lend me a pen.', 'Borrow me a pen'), ('I earn money.', 'I win money'),
 ('Do your homework.', 'Make your homework'), ('I made a mistake.', 'I did a mistake'), ('Remind me later.', 'Remember me later'), ('I’m listening to music.', 'I’m hearing music')])),
'H04': (H, 'in, on, at:\n8 sık hata', '8 sık hata', 'in, on, at seni de yoruyor mu?', hata([
 ('I’m on the bus.', 'In the bus'), ('See you on Monday.', 'In Monday'), ('At night.', 'In the night'), ('I’m at home.', 'In home'),
 ('I’m interested in it.', 'Interested about'), ('On the phone.', 'In the phone'), ('I’m afraid of dogs.', 'Afraid from'), ('Welcome to Istanbul.', 'Welcome in')])),
'H05': (H, 'Türkçe\ndüşününce yapılan\n8 hata', '8 hata', '“Open the light” diyen arkadaşına gönder.', hata([
 ('Turn on the light.', 'Open the light'), ('Turn off the TV.', 'Close the TV'), ('I had a dream.', 'I saw a dream'), ('I don’t smoke.', 'I don’t drink cigarettes'),
 ('I passed the exam.', 'I won the exam'), ('It’s raining.', 'Rain is raining'), ('I feel good.', 'I feel myself good'), ('What does it mean?', 'What is it mean?')])),
'H06': (H, 'Çoğul yaparken\ndüşülen\n8 hata', '8 hata', 'Hangisi seni şaşırttı?', hata([
 ('Some advice.', 'An advice'), ('Information.', 'Informations'), ('Two children.', 'Two childs'), ('My hair is long.', 'My hairs are'),
 ('The news is good.', 'News are'), ('Furniture.', 'Furnitures'), ('Homework.', 'Homeworks'), ('Many people.', 'Much people')])),
'H07': (H, 'Zamanlarda\nyapılan\n8 hata', '8 hata', 'Kaç tanesinde hata yapıyordun?', hata([
 ('I saw it yesterday.', 'I have seen it yesterday'), ('Did you call?', 'Did you called?'), ('She doesn’t know.', 'She don’t know'), ('I’m going now.', 'I go now'),
 ('When I arrive.', 'When I will arrive'), ('I used to play.', 'I use to play'), ('I was born in May.', 'I born in May'), ('I have to go.', 'I must to go')])),
# ---------------- TEMALI KELİMELER ----------------
'T01': (T, 'Havalimanında\nlazım olacak\n8 kelime', '8 kelime', 'Yakında seyahate çıkan birine gönder.', [
 ('boarding pass', 'biniş kartı'), ('gate', 'kapı'), ('carry-on', 'el bagajı'), ('delay', 'rötar'),
 ('layover', 'aktarma beklemesi'), ('customs', 'gümrük'), ('aisle seat', 'koridor koltuğu'), ('baggage claim', 'bagaj teslim')]),
'T02': (T, 'Restoranda\nlazım olacak\n8 kelime', '8 kelime', 'Yurt dışında ilk ne sipariş ederdin?', [
 ('bill', 'hesap'), ('tip', 'bahşiş'), ('starter', 'başlangıç'), ('main course', 'ana yemek'),
 ('dessert', 'tatlı'), ('reservation', 'rezervasyon'), ('takeaway', 'paket servis'), ('waiter', 'garson')]),
}

# Son slayt (yorum çağrısı) – seriye göre alt satır
LAST = {K: 'Sen hangisini eklerdin?', D: 'Sen başka ne derdin?', P: 'Bildiğin bir tane de sen yaz.',
        H: 'Sen en çok hangisini yapıyorsun?', T: 'Sen hangi kelimeyi eklerdin?'}

# 16 hafta: (Pazar, Pazartesi, Çarşamba) + haftanın fiili (Reels fiil serisi için)
WEEKS = [
 ('K01','D01','H01','GET'), ('K02','P01','K03','GET'), ('K04','D02','P02','TAKE'), ('K05','P03','H02','PUT'),
 ('K06','D03','D04','GO'),  ('K07','P04','H03','GO'),  ('K08','D05','K09','LOOK'), ('K10','P05','T01','LOOK'),
 ('K11','D06','H04','COME'),('K12','P06','P07','TURN'),('K13','D07','H05','MAKE'), ('K14','P08','D08','MAKE'),
 ('K15','D09','K16','RUN'), ('K17','P09','H06','RUN'), ('K18','D10','T02','BREAK'),('K19','P10','H07','BREAK'),
]

import datetime as _dt
def PLAN():
    """(hafta, tarih, set kodu, haftanın fiili). 1. hafta: bugün (Sal 6 Eki) + Çar 7 Eki; sonra Paz/Pzt/Çar."""
    out=[(1,_dt.date(2026,10,6),'K01','GET'),(1,_dt.date(2026,10,7),'D01','GET')]
    sun=_dt.date(2026,10,11)
    for i,(a,b,c,v) in enumerate(WEEKS[1:]):
        s=sun+_dt.timedelta(weeks=i)
        out+=[(i+2,s,a,v),(i+2,s+_dt.timedelta(days=1),b,v),(i+2,s+_dt.timedelta(days=3),c,v)]
    out.append((17,sun+_dt.timedelta(weeks=15),'H01','BREAK'))
    return out
