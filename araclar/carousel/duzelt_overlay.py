import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
S=2; FD='/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf'
def F(w,sz): return ImageFont.truetype(''+__import__('os').path.join(__import__('os').path.dirname(__file__),'../fonts/Poppins-SemiBold.ttf')+'' if w=='SemiBold' else FD%w,int(sz*S))
BGC=(255,254,252); INK=(28,26,27); TRC=(40,38,38); OR=(236,124,48); OR2=(228,112,39)
def tw(d,t,f): return d.textlength(t,font=f)
def fit(d,lines,w,start,maxw,mn):
    sz=start
    while sz>mn and max(tw(d,l,F(w,sz)) for l in lines)>maxw*S: sz-=2
    return F(w,sz),sz
def sc(*a): return [v*S for v in a]
def base(src):
    im=Image.open(src).convert('RGB'); im=im.resize((1080*S,1440*S),Image.LANCZOS)
    d=ImageDraw.Draw(im); d.rectangle(sc(135,450,945,1100),fill=BGC); return im,d
def save(im,p): im.resize((1080,1440),Image.LANCZOS).save(p,quality=93,subsampling=0)
def slide(src,en,tr,out,encolor=INK,start=112):
    im,d=base(src)
    fe,se=fit(d,[en],'Bold',start,790,40); ft,st=fit(d,[tr],'Medium',72,780,36)
    lhe=se*1.16; lht=st*1.25; total=lhe+56+8+52+lht; y=760-total/2+10
    d.text((540*S,(y+lhe/2)*S),en,font=fe,fill=encolor,anchor='mm'); y+=lhe+56
    d.rounded_rectangle(sc(424,y,656,y+8),radius=4*S,fill=OR); y+=60
    d.text((540*S,(y+lht/2)*S),tr,font=ft,fill=TRC,anchor='mm'); save(im,out)
def cover(src,title,hl,out):
    im,d=base(src); tl=title.split('\n'); f,sz=fit(d,tl,'Bold',104,790,50); lh=sz*1.2
    total=len(tl)*lh+50+8+50+50; y=760-total/2+10
    for l in tl: d.text((540*S,(y+lh/2)*S),l,font=f,fill=OR2 if l==hl else INK,anchor='mm'); y+=lh
    y+=50; d.rounded_rectangle(sc(424,y,656,y+8),radius=4*S,fill=OR); y+=58
    fk=F('SemiBold',46); t='Kaydır'; w=tw(d,t,fk)/S; x=540-(w+70)/2; cy=y+25
    d.text((x*S,cy*S),t,font=fk,fill=OR2,anchor='lm'); ax=x+w+18
    d.line(sc(ax,cy+2,ax+48,cy+2),fill=OR2,width=6*S)
    d.line(sc(ax+30,cy-14,ax+48,cy+2,ax+30,cy+18),fill=OR2,width=6*S,joint='curve'); save(im,out)
