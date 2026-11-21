import re,json,sys
BAL=open('/home/claude/ada/hikaye/index.html').read()
m=re.search(r'(<span class="w" id="w1">.*?</span></span></span>)',BAL); TEMPLATE=m.group(1)
def bal(id,word,tr,pos,extra=''):
    s=TEMPLATE
    s=s.replace('id="w1"',f'id="{id}"')
    s=re.sub(r'<span class="wbg"></span>.*?<span class="ul">',f'<span class="wbg"></span>{word}<span class="ul">',s,count=1)
    s=re.sub(r'<span class="bal [^"]*">',f'<span class="bal up{extra}">',s)
    s=re.sub(r'<div class="tr">.*?</div><div class="pos">.*?</div>',f'<div class="tr">{tr}</div><div class="pos">{pos}</div>',s)
    return s
def build(path,sents,balloons,taps,end,heading_ids=()):
    # sents: list of (sid, [(text,t)], tend, cls, br_before)
    html=[];W=[];S=[]
    for sid,words,tend,cls,br in sents:
        parts=[];i=0
        while i<len(words):
            txt,t=words[i]
            b=balloons.get((sid,i))
            if b:
                n=b['n']; grp=' '.join(w[0] for w in words[i:i+n]); trail=''
                mm=re.match(r'^(.*?)([.,:;]*)$',grp); core,trail=mm.group(1),mm.group(2)
                wid=f'{sid}_{i}'; parts.append(f'<span class="wd" id="{wid}">'+bal(b['id'],core,b['tr'],b['pos'],b.get('extra',''))+f'</span>{trail}')
                nxt=words[i+n][1] if i+n<len(words) else tend
                W.append([wid,t,nxt]); i+=n; continue
            wid=f'{sid}_{i}'; parts.append(f'<span class="wd" id="{wid}">{txt}</span>')
            nxt=words[i+1][1] if i+1<len(words) else tend
            W.append([wid,t,nxt]); i+=1
        S.append([sid,words[0][1],tend])
        html.append(br+f'<span class="s{cls}" id="{sid}">'+' '.join(parts)+'</span>')
    para=' '.join(html)
    s=open(path).read()
    s=re.sub(r'<div id="para">.*</div></div>\s*<script>',f'<div id="para">{para}</div></div>\n<script>',s,flags=re.S)
    T={"titleAt":-1 if 'reel' in path else 0.25,"paraAt":-1 if 'reel' in path else 0.8,"sent":[],"taps":taps,"end":end}
    s=re.sub(r'const T = \{.*?\};(?: const SENT=.*?\]; const WORDS=.*?\];)?',f'const T = {json.dumps(T)}; const SENT={json.dumps(S)}; const WORDS={json.dumps(W)};',s,count=1,flags=re.S)
    s=s.replace('T.sent.forEach(([a,b], i) => {\n  const s = "#s" + (i+1);','SENT.forEach(([sid,a,b]) => {\n  const s = "#" + sid;')
    if 'WORDS.forEach' not in s:
        s=s.replace('T.taps.forEach','WORDS.forEach(([id,a,b]) => { tl.set("#"+id, {boxShadow:"inset 0 -5px 0 0 #F08C1E"}, a).set("#"+id, {boxShadow:"inset 0 0 0 0 rgba(0,0,0,0)"}, b); });\nT.taps.forEach')
    s=re.sub(r'data-duration="[\d.]+"',f'data-duration="{end}"',s)
    if '.wd{' not in s: s=s.replace('</style></head>','.wd{border-radius:2px}</style></head>',1)
    open(path,'w').write(s)
