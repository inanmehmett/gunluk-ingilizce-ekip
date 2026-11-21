import subprocess,array,sys,json,wave
F="/mnt/user-data/uploads/Video-Kurgu/Uygulama görselleri/ScreenRecording_11-21-2026 00-20-01_1.MP4"
SR=48000
raw=subprocess.run(['ffmpeg','-v','error','-i',F,'-vn','-ac','1','-ar',str(SR),'-f','s16le','-'],capture_output=True).stdout
src=array.array('h',raw)
def build(out,blocks,total,fade=0.15,fo_s=0.25):
    buf=array.array('h',[0])*int(total*SR)
    for a,b,st in blocks:
        seg=src[int(a*SR):int(b*SR)];n=len(seg);fi=int(fade*SR);fo=int(fo_s*SR)
        o=int(st*SR)
        for i in range(n):
            g=1.0
            if i<fi: g=i/fi
            if i>n-fo: g=min(g,(n-i)/fo)
            if o+i<len(buf): buf[o+i]=int(seg[i]*g)
    w=wave.open(out,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(buf.tobytes());w.close()
    subprocess.run(['ffmpeg','-v','error','-y','-i',out,'-af','loudnorm=I=-16:TP=-1.5','-ar','48000','-ac','2',out.replace('.wav','_n.wav')],check=True)
cfg=json.loads(sys.argv[1]); build(cfg["out"],cfg["blocks"],cfg["total"],cfg.get("fade",0.15),cfg.get("fo",0.25))
