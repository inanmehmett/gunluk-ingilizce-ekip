from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
W,H=1080,1920; F='/home/claude/reklam/ad/assets/Literata.ttf'
def font(sz,w=400):
    f=ImageFont.truetype(F,sz); f.set_variation_by_axes([w if a['name']==b'Weight' else (sz/3 if a['name']==b'Optical size' else a['default']) for a in f.get_variation_axes()]); return f
BG=(250,243,234); INK=(34,30,26); GREY=(150,136,118); OR=(240,140,30)
im=Image.new('RGB',(W,H),BG)
cov=Image.open('kapak_kucuk.png').convert('RGB').crop((10,10,110,150))
cov=cov.resize((W,int(W*cov.height/cov.width)),Image.BICUBIC).filter(ImageFilter.GaussianBlur(5))
ch=660; cov=cov.crop((0,40,W,ch+40))
g=Image.linear_gradient('L').resize((W,ch)).point(lambda v: int(max(0,min(255,(v-60)*255/150))))
im.paste(Image.composite(Image.new('RGB',(W,ch),BG),cov,g),(0,0))
d=ImageDraw.Draw(im)
d.text((W/2,620),'Bu akşam ne okuyorsun?',font=font(70,650),fill=INK,anchor='mm')
d.text((W/2,700),'The Happy Prince · Oscar Wilde',font=font(36,500),fill=GREY,anchor='mm')
txt=("One night a little swallow flew over the roofs. His friends had left for the warm south six weeks before. "
     "He had stayed behind, because he loved a reed that grew by the river. The reed was slim and beautiful, "
     "but she never said anything, and she never wanted to travel. So at last the swallow left her and flew away alone.")
SZ=int(sys.argv[1]) if len(sys.argv)>1 else 50; M=int(sys.argv[2]) if len(sys.argv)>2 else 60
f=font(SZ,400); LH=int(SZ*1.62); maxw=W-2*M
lines=[];cur=''
for w in txt.split():
    t=(cur+' '+w).strip()
    if d.textlength(t,font=f)<=maxw: cur=t
    else: lines.append(cur); cur=w
lines.append(cur)
y0=810
# find 'alone'
TG='by the river'; li=[i for i,l in enumerate(lines) if TG in l][0]; pre=lines[li][:lines[li].find(TG)]
ax=M+d.textlength(pre,font=f); aw=d.textlength(TG,font=f); ay=y0+li*LH
print(len(lines),'alone center',ax+aw/2, 'last y',ay)
# highlight
hl=Image.new('RGBA',(W,H),(0,0,0,0)); hd=ImageDraw.Draw(hl)
hd.rounded_rectangle((ax-8,ay-6,ax+aw+2,ay+SZ+18),10,fill=(245,205,150,150))
im.paste(hl,(0,0),hl); d=ImageDraw.Draw(im)
for i,l in enumerate(lines): d.text((M,y0+i*LH),l,font=f,fill=INK)
d.line((ax-6,ay+SZ+18,ax+aw,ay+SZ+18),fill=OR,width=4)
# balloon
bw,bh=720,168; cx=ax+aw/2; bx=int(max(40,min(W-40-bw,cx-bw/2))); by=int(ay-bh-26)
sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
sd.rounded_rectangle((bx,by+14,bx+bw,by+bh+14),40,fill=(90,60,20,70)); sh=sh.filter(ImageFilter.GaussianBlur(26)); im.paste(sh,(0,0),sh)
d=ImageDraw.Draw(im)
d.rounded_rectangle((bx,by,bx+bw,by+bh),40,fill=(255,255,255),outline=(236,224,206),width=2)
d.polygon([(cx-22,by+bh-1),(cx+22,by+bh-1),(cx,by+bh+22)],fill=(255,255,255))
d.text((bx+44,by+14),"nehir kenarında",font=font(54,450),fill=INK)
sf=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',28) 
d.text((bx+46,by+110),"kalıp",font=sf,fill=(140,128,112))
# speaker icon
sx,sy=bx+bw-225,by+bh//2
d.polygon([(sx,sy-10),(sx+12,sy-10),(sx+28,sy-24),(sx+28,sy+24),(sx+12,sy+10),(sx,sy+10)],fill=(130,120,108))
for r in (14,26): d.arc((sx+28-r,sy-r,sx+28+r,sy+r),-45,45,fill=(130,120,108),width=4)
# check button
kx,ky=bx+bw-90,by+bh//2
d.ellipse((kx-44,ky-44,kx+44,ky+44),fill=(253,234,206))
d.line([(kx-18,ky+1),(kx-5,ky+15),(kx+20,ky-13)],fill=(226,110,20),width=6,joint='curve')
im.save('hikaye_uygulama.png'); im.resize((360,640)).save('prev.jpg')
