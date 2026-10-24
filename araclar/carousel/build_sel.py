import os,sys
os.chdir('/home/claude/carousel'); sys.path.insert(0,'/home/claude/carousel')
src=open('build.py').read().split("if '--noimg' not in sys.argv:")[0]
exec(src)
OUT='/home/claude/reels/kasim/carousel'
for code in sys.argv[1:]:
    ser,title,hl,q,items=SETS[code]
    dn=f'{OUT}/{code}'; os.makedirs(dn,exist_ok=True)
    cover(title,hl,f'{dn}/01.jpg',code)
    for i,(en,tr) in enumerate(items,1): slide(en,tr,f'{i}/8',f'{dn}/{i+1:02d}.jpg',code)
    slide('9. ?',LAST[ser],None,f'{dn}/10.jpg',code,encolor=OR2,start=150)
print(small)
