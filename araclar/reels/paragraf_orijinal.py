# Paragraf reeli — 15 Ekim 2026 orijinal şablonu (ölçüler o videodan alındı) + isteğe bağlı "kelimeye dokun" animasyonu.
# kullanım: python3 paragraf_orijinal.py spec.json klip.mp4 cikti.mp4 [onizleme_dizini]
import sys, json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
FONT=os.environ.get('LITERATA', os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','font','Literata.ttf'))
def font(sz,w=400):
    f=ImageFont.truetype(FONT,sz); f.set_variation_by_axes([w if a['name']==b'Weight' else (14 if a['name']==b'Optical size' else a['default']) for a in f.get_variation_axes()]); return f
FE=['lnum','tnum']; INK=(28,28,28,255); PEACH=(249,215,174,255); WHITE=(255,255,255,255); ORANGE=(242,140,40,255)
# orijinalden ölçülen sabitler
HOOK_BOX=(146,664,933,747); HOOK_BASE=718; HOOK_SZ=48
PAR_X0,PAR_X1,PAR_TOP=142,939,760; TEXT_X=168; BASE0=811; STEP=71; PAR_SZ=40; PAD_BOT=20
s=json.load(open(sys.argv[1])); clip,out=sys.argv[2],sys.argv[3]; prevdir=sys.argv[4] if len(sys.argv)>4 else None
dur=float(s.get('sure',10.5)); slow=float(s.get('yavas',0.75)); start=float(s.get('baslangic',0))
lines=s['satirlar']; fp=font(PAR_SZ); fh=font(HOOK_SZ)
base=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
d.rectangle(HOOK_BOX,fill=WHITE); hw=d.textlength(s['hook'],font=fh,features=FE)
assert hw<=HOOK_BOX[2]-HOOK_BOX[0]-40, 'hook sığmıyor'
d.text(((HOOK_BOX[0]+HOOK_BOX[2])/2-hw/2,HOOK_BASE),s['hook'],font=fh,fill=INK,anchor='ls',features=FE)
par_bot=BASE0+STEP*(len(lines)-1)+PAD_BOT; d.rectangle((PAR_X0,PAR_TOP,PAR_X1,par_bot),fill=PEACH)
for i,l in enumerate(lines):
    lw=d.textlength(l,font=fp,features=FE); assert TEXT_X+lw<=PAR_X1-24, 'satır sığmıyor: '+l
    d.text((TEXT_X,BASE0+i*STEP),l,font=fp,fill=INK,anchor='ls',features=FE)
print('grup y',HOOK_BOX[1],'-',par_bot,'| satir',len(lines),'| karakter',sum(len(l) for l in lines))
k=s.get('kelime'); anim=None
if k:
    li=k['satir']-1; l=lines[li]; i0=l.index(k['yazi']); wx0=TEXT_X+d.textlength(l[:i0],font=fp,features=FE); wx1=wx0+d.textlength(k['yazi'],font=fp,features=FE); wb=BASE0+li*STEP
    # balon (2x çizilip küçültülür)
    S=2; fm=font(30*S,430); fs=ImageFont.truetype(FONT,19*S); tw=int(d.textlength(k['anlam'],font=font(30,430),features=FE))
    bw,bh=24+tw+20+34+16+46+16, 82; im=Image.new('RGBA',((bw+60)*S,(bh+60)*S),(0,0,0,0))
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((30*S,36*S,(30+bw)*S,(36+bh)*S),radius=26*S,fill=(0,0,0,70)); im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(12*S)))
    b=ImageDraw.Draw(im); ox,oy=30*S,30*S; b.rounded_rectangle((ox,oy,ox+bw*S,oy+bh*S),radius=26*S,fill=WHITE)
    b.text((ox+24*S,oy+41*S),k['anlam'],font=fm,fill=INK,anchor='ls',features=FE); b.text((ox+25*S,oy+66*S),k.get('tur','fiil'),font=fs,fill=(150,150,150,255),anchor='ls')
    sx=ox+(24+tw+20)*S; cy=oy+bh*S//2; g=(150,150,150,255)   # hoparlör
    b.polygon([(sx,cy-6*S),(sx+8*S,cy-6*S),(sx+17*S,cy-14*S),(sx+17*S,cy+14*S),(sx+8*S,cy+6*S),(sx,cy+6*S)],fill=g)
    b.arc((sx+12*S,cy-10*S,sx+28*S,cy+10*S),-50,50,fill=g,width=3*S); b.arc((sx+10*S,cy-16*S,sx+36*S,cy+16*S),-45,45,fill=g,width=3*S)
    px=ox+(24+tw+20+34+16)*S; b.ellipse((px,cy-23*S,px+46*S,cy+23*S),fill=ORANGE)   # turuncu +
    b.line((px+13*S,cy,px+33*S,cy),fill=WHITE,width=5*S); b.line((px+23*S,cy-10*S,px+23*S,cy+10*S),fill=WHITE,width=5*S)
    bub=im.resize((bw+60,bh+60),Image.LANCZOS)
    cx=(wx0+wx1)/2; bx=min(max(cx-bw/2,PAR_X0+10),PAR_X1-10-bw); by=wb-34-10-bh   # kelimenin üstünde
    anim=dict(wx0=wx0,wx1=wx1,wb=wb,cx=cx,bub=bub,bx=bx-30,by=by-30,bw=bw,bh=bh,t=float(k.get('dokunma',3.5)),bitis=float(k.get('bitis',7.5)))
    print('kelime',k['yazi'],'x',round(wx0),round(wx1),'taban',wb,'| balon x',round(bx),round(bx+bw),'y',round(by),round(by+bh))
def ease(x): x=min(max(x,0),1); return 1-(1-x)**3
def frame(t):
    if not anim or t<anim['t']-0.05 or t>anim['bitis']+0.35: return base
    a=anim; im=base.copy(); t0=a['t']; fo=1-min(max((t-a['bitis'])/0.3,0),1)
    u=ease((t-t0)/0.2)
    if u>0 and fo>0:
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(ov).rectangle((a['wx0'],a['wb']+7,a['wx0']+(a['wx1']-a['wx0'])*u,a['wb']+11),fill=ORANGE[:3]+(int(255*fo),)); im=Image.alpha_composite(im,ov)
    r=(t-(t0-0.05))/0.4
    if 0<=r<=1:
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); rad=18+30*ease(r); ImageDraw.Draw(ov).ellipse((a['cx']-rad,a['wb']-14-rad,a['cx']+rad,a['wb']-14+rad),fill=(40,40,40,int(85*(1-r)))); im=Image.alpha_composite(im,ov)
    bi=ease((t-(t0+0.3))/0.25)
    if bi>0 and fo>0:
        sc=0.92+0.08*bi; bb=a['bub']; nw,nh=int(bb.width*sc),int(bb.height*sc); bb=bb.resize((nw,nh),Image.LANCZOS)
        al=bb.getchannel('A').point(lambda v:int(v*bi*fo)); bb.putalpha(al)
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); ov.paste(bb,(int(a['bx']+(a['bub'].width-nw)/2),int(a['by']+(a['bub'].height-nh))),bb); im=Image.alpha_composite(im,ov)
    return im
n=int(round(dur*FPS)); pre=f"setpts=PTS/{slow}," if slow!=1 else ""
vf=f"[0:v]{pre}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS},format=yuv420p[bg];[bg][1:v]overlay=0:0:format=auto,format=yuv420p[v]"
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-ss',str(start),'-t',str(round(dur*slow+0.3,2)),'-i',clip,'-f','rawvideo','-pix_fmt','rgba','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-filter_complex',vf,'-map','[v]','-t',str(dur),
    '-c:v','libx264','-preset','slow','-crf','19','-profile:v','high','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-an','-movflags','+faststart',out],stdin=subprocess.PIPE)
bb=base.tobytes()
for i in range(n):
    f=frame(i/FPS); p.stdin.write(bb if f is base else f.tobytes())
p.stdin.close(); assert p.wait()==0
if prevdir:
    for nm,t in (('ilk-kare',0.2),('dokunma',anim['t']+0.15 if anim else 1),('balon',anim['t']+1.5 if anim else 2)):
        subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',out,'-frames:v','1',os.path.join(prevdir,nm+'.png')],check=True)
print('bitti',out,round(os.path.getsize(out)/1e6,1),'MB')
