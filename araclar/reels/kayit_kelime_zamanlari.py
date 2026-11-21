import subprocess,sys,json
F="/mnt/user-data/uploads/Video-Kurgu/Uygulama görselleri/ScreenRecording_11-21-2026 00-20-01_1.MP4"
W,H=585,1266;FPS=25;YA,YB=150,1000
def track(t0,t1):
    p=subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',F,'-vf',f'fps={FPS},scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    fs=W*H*3;out=[]
    for k in range(len(p)//fs):
        fr=p[k*fs:(k+1)*fs];xs=[];ys=[]
        for y in range(YA,YB):
            row=fr[y*W*3:(y+1)*W*3]
            for x in range(0,W,2):
                r,g,b=row[x*3],row[x*3+1],row[x*3+2]
                if r>200 and 80<g<170 and b<90: xs.append(x);ys.append(y)
        t=round(t0+k/FPS,3)
        if len(xs)>15 and max(ys)-min(ys)<=5: out.append((t,min(xs),max(xs),min(ys)))
        else: out.append((t,None))
    return out
res={}
for a,b in json.loads(sys.argv[1]): res[f'{a}-{b}']=track(a,b)
json.dump(res,open(sys.argv[2],'w'))
