import os, re, shutil, datetime as dt, zipfile, sys
src=open('gen.py').read().split("sets={")[0]; exec(src)
from data import SETS, LAST, WEEKS
GUN={6:'Paz',0:'Pzt',1:'Sal',2:'Car'}
BG=base(None)[0]
small=[]
def canvas(counter):
    im=BG.copy(); d=ImageDraw.Draw(im)
    if counter: d.text((58*S,62*S),counter,font=F('Medium',56),fill='white',anchor='mm' if 0 else 'lm')
    return im,d
def save(im,path): im.resize((W,H),Image.LANCZOS).save(path,quality=93,subsampling=0)
def slide(en,tr,counter,path,tag,encolor=INK,start=112):
    im,d=canvas(counter)
    fe,se=fit(d,[en],'Bold',start,790,40); ft,st=fit(d,[tr],'Medium',72,780,36)
    if tw(d,en,fe)>790*S or tw(d,tr,ft)>780*S: small.append(('TASMA',tag,en,tr))
    if se<68 or st<50: small.append((se,st,tag,en,tr))
    lhe=se*1.16; lht=st*1.25; total=lhe+56+8+52+lht; y=760-total/2+10
    d.text((540*S,(y+lhe/2)*S),en,font=fe,fill=encolor,anchor='mm'); y+=lhe+56
    d.rounded_rectangle(sc(424,y,656,y+8),radius=4*S,fill=OR); y+=60
    d.text((540*S,(y+lht/2)*S),tr,font=ft,fill=(40,38,38),anchor='mm')
    save(im,path)
def cover(title,hl,path,tag):
    im,d=canvas(None)
    tl=title.split('\n'); f,sz=fit(d,tl,'Bold',104,790,50); lh=sz*1.2
    if sz<70: small.append((sz,'kapak',tag,title))
    total=len(tl)*lh+50+8+50+50; y=760-total/2+10
    for l in tl:
        d.text((540*S,(y+lh/2)*S),l,font=f,fill=OR2 if l==hl else INK,anchor='mm'); y+=lh
    y+=50; d.rounded_rectangle(sc(424,y,656,y+8),radius=4*S,fill=OR); y+=58
    fk=F('SemiBold',46); t='Kaydır'; w=tw(d,t,fk)/S; x=540-(w+70)/2; cy=y+25
    d.text((x*S,cy*S),t,font=fk,fill=OR2,anchor='lm'); ax=x+w+18
    d.line(sc(ax,cy+2,ax+48,cy+2),fill=OR2,width=6*S)
    d.line(sc(ax+30,cy-14,ax+48,cy+2,ax+30,cy+18),fill=OR2,width=6*S,joint='curve')
    save(im,path)
# --- kontroller
seen={}; dups=[]
for k,(ser,title,hl,q,items) in SETS.items():
    assert len(items)==8,(k,len(items)); assert hl in title.split('\n'),(k,hl)
    for en,tr in items:
        n=re.sub(r'[^a-z ]','',en.lower().replace('’',''))
        if n in seen: dups.append((n,seen[n],k))
        seen[n]=k
used=[c for w in WEEKS for c in w[:3]]
assert sorted(used)==sorted(SETS), set(SETS)^set(used)
print('set',len(SETS),'ifade',len(seen),'tekrar',dups)
# --- takvim
from data import PLAN
plan=PLAN()
if '--noimg' not in sys.argv:
    shutil.rmtree('out',ignore_errors=True)
    for wk,date,code,verb in plan:
        ser,title,hl,q,items=SETS[code]
        dn=f'out/H{wk:02d}_{date.isoformat()}_{GUN[date.weekday()]}_{code}'; os.makedirs(dn)
        cover(title,hl,f'{dn}/01.jpg',code)
        for i,(en,tr) in enumerate(items,1): slide(en,tr,f'{i}/8',f'{dn}/{i+1:02d}.jpg',code)
        slide('9. ?',LAST[ser],None,f'{dn}/10.jpg',code,encolor=OR2,start=150)
        open(f'{dn}/aciklama.txt','w').write(caption(q) if 0 else q+'\n\nKaydet, lazım olunca elinin altında olsun 📌\n\n#ingilizce #ingilizceöğren #günlükingilizce')
    for s in small: print(s)
    for z in range(4):
      if True:
        with zipfile.ZipFile(f'carousel_hafta_{z*4+1:02d}-{z*4+4:02d}.zip','w',zipfile.ZIP_STORED) as zf:
            for dn in sorted(os.listdir('out')):
                if z*4+1<=min(int(dn[1:3]),16)<=z*4+4:
                    for fn in sorted(os.listdir('out/'+dn)): zf.write(f'out/{dn}/{fn}',f'{dn}/{fn}')
    os.system('ls -la *.zip; ls out | wc -l; find out -name "*.jpg" | wc -l')
