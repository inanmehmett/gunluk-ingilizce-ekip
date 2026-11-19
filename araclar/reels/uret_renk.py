# Klip bazında renk ayarı + şablon render. kullanım: python3 _uret2.py PROJE KLIP CIKTI [sablon=paragraf|buyuk "s1|s2"] [sure]
import sys,os,json,subprocess,statistics as st
P,C,O=sys.argv[1],sys.argv[2],sys.argv[3]; mod=sys.argv[4] if len(sys.argv)>4 else 'paragraf'
os.chdir(os.path.expanduser('~/mnt/Video-Kurgu/02_Projeler')); os.makedirs(f'{P}/ham',exist_ok=True); os.makedirs(f'{P}/cikti',exist_ok=True)
src=[x for x in os.listdir('../01_Ham-Malzeme') if x.split('.')[0]==C][0]; src='../01_Ham-Malzeme/'+src
pr=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=color_transfer,r_frame_rate:format=duration','-of','json',src],capture_output=True,text=True); j=json.loads(pr.stdout)
hdr=j['streams'][0].get('color_transfer','') in ('arib-std-b67','smpte2084'); dur=float(j['format']['duration'])
base="scale=1080:1920:force_original_aspect_ratio=increase:flags=bicubic,crop=1080:1920"
tm=",zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" if hdr else ""
# ölçüm: 5 kare, ortalama parlaklık (Y) ve doygunluk (U,V sapması)
Ys=[];Ss=[]
for t in [dur*x for x in (0.1,0.3,0.5,0.7,0.9)]:
    raw=subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',src,'-frames:v','1','-vf',base.replace('1080:1920','108:192')+tm+',format=yuv444p','-f','rawvideo','-'],capture_output=True).stdout
    n=108*192; 
    if len(raw)<3*n: continue
    Y=raw[:n];U=raw[n:2*n];V=raw[2*n:3*n]
    Ys.append(sum(Y)/n); Ss.append(sum(abs(u-128)+abs(v-128) for u,v in zip(U,V))/n)
y=st.mean(Ys); s=st.mean(Ss)
import math
hedefY=118.0
gamma=max(0.8,min(1.45, math.log(max(y,1)/255)/math.log(hedefY/255)))   # eq gamma>1 aydınlatır
sat=1.18 if s<14 else (1.05 if s>30 else round(1.18-(s-14)/16*0.13,2))
kon=1.06 if (max(Ys)-min(Ys))<12 else 1.04
g=f"{base}{tm},eq=gamma={gamma:.2f}:contrast={kon}:saturation={sat},colortemperature=temperature=5600:mix=0.6"
print(f'{C}: hdr={hdr} Y={y:.0f} doygunluk={s:.1f} -> gamma={gamma:.2f} sat={sat} kontrast={kon}')
tmp=f'{P}/ham/g_tmp.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-ss','0.3','-i',src,'-t','9.6','-vf',g,'-c:v','libx264','-preset','ultrafast','-crf','14','-an',tmp],check=True); os.replace(tmp,f'{P}/ham/g2.mp4')
L='../03_Varliklar/font/Literata.ttf'; env=dict(os.environ,LITERATA=os.path.abspath(L))
out=f'{P}/cikti/{O}_tmp.mp4'
if mod=='paragraf':
    subprocess.run(['python3','../03_Varliklar/sablon/paragraf_orijinal.py',f'{P}/kurgu/spec.json',f'{P}/ham/g2.mp4',out,f'{P}/cikti'],check=True,env=env)
else:
    subprocess.run(['python3','../03_Varliklar/sablon/buyuk_yazi.py',sys.argv[5],f'{P}/ham/g2.mp4',out,sys.argv[6]],check=True,env=env)
os.replace(out,f'{P}/cikti/{O}.mp4')
subprocess.run(['ffmpeg','-v','error','-y','-ss','0.2','-i',f'{P}/cikti/{O}.mp4','-frames:v','1','-vf','scale=270:-1',f'{P}/cikti/k2.jpg'],check=True)
# önce/sonra: ham (sadece kırpma) vs yeni
subprocess.run(['ffmpeg','-v','error','-y','-ss','2','-i',src,'-frames:v','1','-vf',base+tm+',scale=270:-1',f'{P}/cikti/once.jpg'],check=True)
print('bitti',O)
