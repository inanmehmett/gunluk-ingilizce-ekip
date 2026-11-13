# D1 "büyük yazı" reeli: tek büyük Türkçe hook, beyaz kutular (satır arası boşluksuz), Literata 600; içerik açıklamada. Sıralı belirme yok.
# kullanım: LITERATA=... python3 buyuk_yazi.py "satır1|satır2|satır3" klip.mp4 cikti.mp4 sure
import sys, os, subprocess
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920; FONT=os.environ['LITERATA']; lines=sys.argv[1].split('|'); clip,out,dur=sys.argv[2],sys.argv[3],float(sys.argv[4])
f=ImageFont.truetype(FONT,66); f.set_variation_by_axes([600 if a['name']==b'Weight' else (14 if a['name']==b'Optical size' else a['default']) for a in f.get_variation_axes()])
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); step=100; padx=30; top=int(H*0.40)-len(lines)*step//2
for i,l in enumerate(lines):
    w=d.textlength(l,font=f); assert w<W-120,'sığmıyor: '+l; x=(W-w)/2; y=top+i*step
    d.rectangle((x-padx,y,x+w+padx,y+step+1),fill=(255,255,255,255)); d.text((W/2,y+step/2+4),l,font=f,fill=(28,28,28,255),anchor='mm',features=['lnum'])
im.save('/tmp/ov.png')
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',clip,'-i','/tmp/ov.png','-filter_complex','[0:v]scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,fps=30,format=yuv420p[bg];[bg][1:v]overlay=0:0,format=yuv420p[v]','-map','[v]','-t',str(dur),'-c:v','libx264','-preset','slow','-crf','19','-pix_fmt','yuv420p','-an','-movflags','+faststart',out],check=True)
print('bitti',out)
