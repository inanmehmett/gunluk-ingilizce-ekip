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

# Kare 1 — doğrudan istek (App Store link çıkartması okun altına)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,380,"Daily English'i kullanıyorsan senden küçük bir şey isteyeceğim:",font(64,600),92)
y=block(d,y+50,"Ne düşündüğünü mağazaya yaz.\nİyi ya da kötü, fark etmez.",font(52,450),80)
y=block(d,y+40,"Hepsini okuyorum; düzeltmem gerekenleri oradan öğreniyorum. Senin birkaç cümlen, uygulamayı ilk kez gören birine de yol gösterir.",font(44,420),68,GREY)
arrow(d,y+60); print('k1 sticker y≈',y+190)
save(im,'v2_1_istek_ios.png')

# Kare 2 — Android (Play 1.0.4 yayına girince)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,560,"Android'de mi kullanıyorsun?",font(64,600),92)
y=block(d,y+20,"Burası:",font(52,450),80,GREY)
arrow(d,y+60)
save(im,'v2_2_android.png')

# Ertesi gün — teşekkür (alıntı yok)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
y=block(d,640,"Yazanlara teşekkürler.",font(72,650),100)
y=block(d,y+30,"Hepsini tek tek okuyorum.",font(52,450),80,GREY)
save(im,'v2_3_tesekkur.png')

sheet=Image.new('RGB',(3*360+40,640),(200,200,200))
for i,n in enumerate(['v2_1_istek_ios.png','v2_2_android.png','v2_3_tesekkur.png']):
    sheet.paste(Image.open(n).resize((360,640)),(10+i*370,0))
sheet.save('v2_sheet.jpg',quality=88)
