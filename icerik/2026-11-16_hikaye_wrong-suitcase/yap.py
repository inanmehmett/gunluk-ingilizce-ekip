from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920; FONT='/home/claude/gunluk-ingilizce-ekip/araclar/fonts/Literata.ttf'
def font(sz,w=400):
    f=ImageFont.truetype(FONT,sz); f.set_variation_by_axes([w if a['name']==b'Weight' else (14 if a['name']==b'Optical size' else a['default']) for a in f.get_variation_axes()]); return f
BG=(249,243,234); INK=(28,28,28); PEACH=(249,215,174); ORANGE=(240,150,55); GREY=(150,138,122)
def wrap(d,text,f,maxw):
    lines=[]; cur=[]
    for w in text.split():
        if d.textlength(' '.join(cur+[w]),font=f)<=maxw: cur.append(w)
        else: lines.append(cur); cur=[w]
    lines.append(cur); return lines
def kare(n,ust,metin,kelime,anlam,hook=None,alt=None,off=None):
    if off is None:
        yy=kare(n,ust,metin,kelime,anlam,hook,alt,0); return kare(n,ust,metin,kelime,anlam,hook,alt,max(0,(1500-yy)//2))
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); fp=font(56); fs=font(30,600); fb=font(40,600)
    d.text((W/2,300+off),ust,font=fs,fill=GREY,anchor='mm')
    y=380+off
    if hook:
        fh=font(60,700)
        for l in hook.split('|'):
            w=d.textlength(l,font=fh); d.rectangle((W/2-w/2-28,y,W/2+w/2+28,y+97),fill=(255,255,255)); d.text((W/2,y+50),l,font=fh,fill=INK,anchor='mm'); y+=96
        y+=70
    x0=100; step=88
    for para in metin.split('\n'):
        for ln in wrap(d,para,fp,W-2*x0):
            has=bool(kelime) and any(kelime in w for w in ln)
            if has: y+=78
            x=x0
            for w in ln:
                ww=d.textlength(w,font=fp)
                if kelime and kelime in w:
                    px=d.textlength(w[:w.index(kelime)],font=fp); x+=px; kw=d.textlength(kelime,font=fp); d.rounded_rectangle((x-8,y+4,x+kw+8,y+76),10,fill=PEACH)
                    bw=d.textlength(anlam,font=fb)+56; cx=x+kw/2; bx=min(max(cx-bw/2,60),W-60-bw)
                    d.rounded_rectangle((bx,y-92,bx+bw,y-16),22,fill=INK); d.polygon([(cx-14,y-18),(cx+14,y-18),(cx,y+2)],fill=INK)
                    d.text((bx+bw/2,y-54),anlam,font=fb,fill=(255,255,255),anchor='mm'); x-=px
                d.text((x,y+40),w,font=fp,fill=INK,anchor='lm'); x+=ww+d.textlength(' ',font=fp)
            y+=step
        y+=34
    if alt: d.text((W/2,y+50),alt,font=font(40,600),fill=ORANGE,anchor='mm')
    assert y<1620,(n,y); im.save(f'hikaye_{n}.png'); return y
T='THE WRONG SUITCASE'
kare(1,T+' · 1/4','I got home from the airport at midnight. I was exhausted.\nI opened my suitcase to find my pajamas.\nBut these were not my clothes.',None,None,hook='Bu hikâyeyi sözlüksüz|bitirebilen var mı?')
kare(2,T+' · 2/4','Inside, there was a blue dress, a camera, and an old notebook.\nOn the first page, someone wrote:\n“If you find this, please don’t call the airline.”',None,None)
kare(3,T+' · 3/4','“Call me.”\nBelow, there was a phone number. I was curious.\nIt was late, but I called. A woman answered after one ring.',None,None)
kare(4,T+' · 4/4','“Finally,” she said. “I have your suitcase too. And I opened it.”\n“We need to talk about the letter in your bag.”\nI didn’t have a letter in my bag.',None,None)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); fp=font(60); fb=font(40,600)
d.text((W/2,470),'Takıldığın kelime',font=font(60,700),fill=INK,anchor='mm'); d.text((W/2,555),'bunlardan biri miydi?',font=font(60,700),fill=INK,anchor='mm')
for j,(k,a) in enumerate([('exhausted','bitkin'),('airline','havayolu şirketi'),('curious','meraklı'),('finally','nihayet')]):
    y=790+j*210; kw=d.textlength(k,font=fp); x=W/2-kw/2; d.rounded_rectangle((x-10,y+2,x+kw+10,y+80),10,fill=PEACH)
    bw=d.textlength(a,font=fb)+56; d.rounded_rectangle((W/2-bw/2,y-92,W/2+bw/2,y-16),22,fill=INK); d.polygon([(W/2-14,y-18),(W/2+14,y-18),(W/2,y+2)],fill=INK)
    d.text((W/2,y-54),a,font=fb,fill=(255,255,255),anchor='mm'); d.text((W/2,y+42),k,font=fp,fill=INK,anchor='mm')
im.save('hikaye_5.png')
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
for i,(t,sz,w,c) in enumerate([('Mektup kimin?',76,700,INK),('Hikâyenin sonu yarın burada.',46,400,INK),('',10,400,INK),('Beklemek istemeyenlere:',40,400,GREY),('böyle hikâyeler her gün',46,600,INK),('Daily English’te 🧡'.replace(' 🧡',''),60,700,ORANGE)]):
    d.text((W/2,640+i*110),t,font=font(sz,w),fill=c,anchor='mm')
im.save('hikaye_6.png')
s=Image.new('RGB',(6*270,480),BG)
for i in range(6): s.paste(Image.open(f'hikaye_{i+1}.png').resize((270,480)),(i*270,0))
s.save('sheet.jpg',quality=85)
