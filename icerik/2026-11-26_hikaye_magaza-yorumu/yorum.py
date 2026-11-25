from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920; F='/home/claude/reklam/ad/assets/Literata.ttf'
def font(sz,w=400):
    f=ImageFont.truetype(F,sz); f.set_variation_by_axes([w if a['name']==b'Weight' else (min(72,max(7,sz/3)) if a['name']==b'Optical size' else a['default']) for a in f.get_variation_axes()]); return f
BG=(250,243,234); INK=(34,30,26); GREY=(140,126,108); OR=(240,140,30)
M=96

def wrap(d,txt,f,maxw):
    out=[]
    for para in txt.split('\n'):
        cur=''
        for w in para.split():
            t=(cur+' '+w).strip()
            if d.textlength(t,font=f)<=maxw: cur=t
            else: out.append(cur); cur=w
        out.append(cur)
    return out

def block(d,y,txt,f,lh,fill=INK,maxw=W-2*M,x=M):
    for l in wrap(d,txt,f,maxw):
        d.text((x,y),l,font=f,fill=fill); y+=lh
    return y

def card(im,y,quote,who):
    d=ImageDraw.Draw(im); fq=font(46,420); lh=72; cw=W-2*M+40; x=M-20
    lines=wrap(d,quote,fq,cw-120)
    ch=110+len(lines)*lh+110
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.rounded_rectangle((x,y+16,x+cw,y+ch+16),44,fill=(90,60,20,60)); sh=sh.filter(ImageFilter.GaussianBlur(28)); im.paste(sh,(0,0),sh)
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((x,y,x+cw,y+ch),44,fill=(255,255,255),outline=(236,224,206),width=2)
    d.text((x+44,y-6),'“',font=font(150,700),fill=OR)
    yy=y+110
    for l in lines: d.text((x+60,yy),l,font=fq,fill=INK); yy+=lh
    d.text((x+60,yy+28),who,font=font(32,500),fill=GREY)
    return y+ch

def arrow(d,y):
    cx=W/2; d.line((cx,y,cx,y+70),fill=OR,width=6); d.polygon([(cx-20,y+56),(cx+20,y+56),(cx,y+86)],fill=OR)

def save(im,n):
    im.save(n); print(n)

# Kare 1 — hikaye + gerçek yorum
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,430,"8 yıldır bu hesaptayım.\nBir süredir de bir uygulama yapıyorum: Daily English.",font(64,600),92)
y=block(d,y+40,"Mağazaya şöyle bir yorum yazılmış:",font(46,420),70,GREY)
card(im,y+70,"Program gündelik hayatta kelimelerin cümle içerisinde hangi anlamda kullanıldığını göstermesi açısından çok iyi. Öğreticiliği mükemmel.","App Store'da bir kullanıcı · 31 Ekim")
save(im,'yorum_1.png')

# Kare 2 — istek (App Store link çıkartması alttaki boşluğa)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,330,"Daily English'i kullanıyorsan bir dakikanı isteyeceğim:",font(64,600),92)
y=block(d,y+50,"Ne düşündüğünü mağazaya yaz.\nİyi ya da kötü, fark etmez.",font(52,450),80)
y=block(d,y+40,"Düzeltmem gerekenleri de oradan öğreniyorum.",font(46,420),70,GREY)
arrow(d,y+70); print('k2 sticker y≈',y+200)
save(im,'yorum_2_ios.png')

# Kare 3 — Android (Play 1.0.4 yayına girince)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,560,"Android'de mi kullanıyorsun?",font(64,600),92)
y=block(d,y+20,"Burası:",font(52,450),80,GREY)
arrow(d,y+60)
save(im,'yorum_3_android.png')

# Ertesi gün — teşekkür
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,560,"Okudum. Teşekkürler.",font(72,650),100)
card(im,y+80,"Tasarımı gerçekten çok hoşuma gitti. Gereksiz özelliklerle dolu değil. Okumaya odaklanabiliyorum. Gelişmeye devam etmesini isterim.","App Store'da bir kullanıcı · 1 Kasım")
save(im,'yorum_4_tesekkur.png')

sheet=Image.new('RGB',(4*360+50,640),(200,200,200))
for i,n in enumerate(['yorum_1.png','yorum_2_ios.png','yorum_3_android.png','yorum_4_tesekkur.png']):
    sheet.paste(Image.open(n).resize((360,640)),(10+i*370,0))
sheet.save('yorum_sheet.jpg',quality=88)
