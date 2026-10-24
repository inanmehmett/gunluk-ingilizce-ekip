"""Static reel in the account's own Instagram look (v3).
- serif font matched to the account's IG text (Literata), flat square boxes, no shadow
- content group centred exactly in the frame (equal space above and below)
- inside each box, padding measured on the real ink so top and bottom gaps are equal
usage: python3 render_v3.py spec.json clip out.mp4 start dur [preview.png]
spec: {"blocks":[{"box":"#ffffff","ink":"#1c1c1c","size":58,"align":"center"|"left","lines":["..",".."],"after":14,"pad":[26,18],"gap":12}]}
"""
import sys, json, subprocess
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = '/home/claude/fonts/dl/Literata.ttf'
def font(sz, w=430):
    f = ImageFont.truetype(FONT, sz)
    vals = [w if a['name'] == b'Weight' else (14 if a['name'] == b'Optical size' else a['default'])
            for a in f.get_variation_axes()]
    f.set_variation_by_axes(vals); return f
def hexc(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (255,)

spec = json.load(open(sys.argv[1])); clip, out = sys.argv[2], sys.argv[3]
start, dur = float(sys.argv[4]), float(sys.argv[5]); prev = sys.argv[6] if len(sys.argv) > 6 else None
d0 = ImageDraw.Draw(Image.new('RGB', (10, 10)))

laid = []
for b in spec['blocks']:
    f = font(b['size'], b.get('wght', 430)); pd = b.get('pad', [26, 18]); padx, pady = pd[0], pd[1]; padb = pd[2] if len(pd) > 2 else pd[1]; gap = b.get('gap', int(b['size'] * .22))
    # baseline-to-baseline step and ink extents (cap/ascender top of first line, baseline/descender of last)
    asc, desc = f.getmetrics(); step = asc + desc + gap
    widths = [d0.textlength(l, font=f, features=['lnum','tnum']) for l in b['lines']]
    meas = ['Hdgy'] * len(b['lines']) if b.get('fixed_ink') else b['lines']   # fixed_ink: same ink box for every line (stacked blocks stay even)
    tops = [d0.textbbox((0, 0), l, font=f, anchor='ls', features=['lnum','tnum'])[1] for l in meas]   # negative: ink above baseline
    bots = [d0.textbbox((0, 0), l, font=f, anchor='ls', features=['lnum','tnum'])[3] for l in meas]   # ink below baseline
    ink_top = tops[0]; ink_bot = (len(b['lines']) - 1) * step + max(bots[-1], 0)
    ink_h = ink_bot - ink_top
    bw = max(widths) + 2 * padx; bh = ink_h + pady + padb
    assert bw <= W - 60, f'too wide {bw:.0f}'
    laid.append((b, f, widths, step, ink_top, bw, bh, padx, pady))
if spec.get('equal_width'):                       # all boxes as wide as the widest one
    mw = max(x[5] for x in laid); laid = [x[:5] + (mw,) + x[6:] for x in laid]
total = sum(x[6] for x in laid) + sum(x[0].get('after', 14) for x in laid[:-1])
y = round((H - total) / 2)                       # equal space above and below the whole group
im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
for b, f, widths, step, ink_top, bw, bh, padx, pady in laid:
    x = round((W - bw) / 2)
    if b.get('pos') == 'left': x = b.get('margin', 130)
    if b.get('pos') == 'right': x = W - bw - b.get('margin', 130)
    if b.get('hidden'):                          # keeps its space (layout stays fixed) but is not drawn yet
        y += bh + b.get('after', 14); continue
    d.rectangle((x, y, x + bw, y + bh), fill=hexc(b['box']))
    base = y + pady - ink_top                     # first baseline so ink starts exactly pady below box top
    for i, (l, lw) in enumerate(zip(b['lines'], widths)):
        tx = x + (bw - lw) / 2 if b.get('align', 'center') == 'center' else x + padx
        if b.get('mask') and ' – ' in l: l = l.split(' – ')[0]   # reveal later: draw word only, box keeps full size
        d.text((tx, base + i * step), l, font=f, fill=hexc(b.get('ink', '#1c1c1c')), anchor='ls', features=['lnum','tnum'])
    y += bh + b.get('after', 14)
im.save('/home/claude/reels/tmp_overlay3.png')
import os
SLOW = float(os.environ.get('SLOW', '1'))      # 0.75 = play clip at 75% speed (calmer, longer)
PUSH = float(os.environ.get('PUSH', '0'))      # 0.04 = "Görünmez Dikiş": bg zooms 1→1.04→1 (sin) over the loop
pre = f"setpts=PTS/{SLOW}," if SLOW != 1 else ""
push = (f",scale=w='trunc({W}*(1+{PUSH}*sin(PI*t/{dur}))/2)*2':h='trunc({H}*(1+{PUSH}*sin(PI*t/{dur}))/2)*2':eval=frame:flags=bicubic,crop={W}:{H}"
        if PUSH else "")
vf = (f"[0:v]{pre}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H}{push},fps=30,format=yuv420p[bg];"
      f"[bg][1:v]overlay=0:0,format=yuv420p[v]")
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(start), '-t', str(round(dur*SLOW+0.2,2)), '-i', clip, '-loop', '1', '-i',
                '/home/claude/reels/tmp_overlay3.png', '-filter_complex', vf, '-map', '[v]', '-t', str(dur),
                '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
                '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an', '-movflags', '+faststart', out], check=True)
if prev: subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '0.1', '-i', out, '-frames:v', '1', prev], check=True)
print(out, 'group top', round((H - total) / 2), 'group bottom', round((H - total) / 2) + total)
