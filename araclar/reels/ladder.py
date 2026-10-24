"""Seviye merdiveni reel overlay: ladder strip + hook (with emoji) + text box. Static.
usage: python3 ladder.py step(1-6) clip start dur out.mp4"""
import sys, subprocess
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = '/home/claude/fonts/dl/Literata.ttf'
FE = ['lnum', 'tnum']
def font(sz, w=430):
    f = ImageFont.truetype(FONT, sz)
    f.set_variation_by_axes([w if a['name'] == b'Weight' else (14 if a['name'] == b'Optical size' else a['default'])
                             for a in f.get_variation_axes()]); return f
EF = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf', 109)
def emoji(ch, h):
    im = Image.new('RGBA', (220, 220), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), ch, font=EF, embedded_color=True)
    im = im.crop(im.getbbox()); return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
WHITE, PEACH, INK, ORANGE, MUTED = (255,)*4, (249, 215, 174, 255), (28, 28, 28, 255), (224, 98, 47, 255), (150, 120, 95, 255)
LEVELS = ['A1', 'A2', 'A2+', 'B1', 'B1+', 'B2']

def build(step, hook_lines, hook_emoji, text_lines, out_png):
    d0 = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    fl, fh, ft = font(30, 600), font(46, 560), font(41)
    BOXW = 920; x0 = (W - BOXW) // 2
    # heights
    lad_h = 92
    hstep = 62; hook_h = 30 + hstep * len(hook_lines) + 18
    tstep = 57; text_h = 34 + tstep * len(text_lines) + 14
    gap = 14
    total = lad_h + gap + hook_h + gap + text_h
    y = (H - total) // 2
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    # ladder strip
    d.rectangle((x0, y, x0 + BOXW, y + lad_h), fill=PEACH)
    n = len(LEVELS); pad = 70; span = BOXW - 2 * pad; cy = y + 32
    xs = [x0 + pad + span * i / (n - 1) for i in range(n)]
    d.line((xs[0], cy, xs[-1], cy), fill=MUTED, width=3)
    if step > 1: d.line((xs[0], cy, xs[step - 1], cy), fill=ORANGE, width=5)
    for i, (cx, lv) in enumerate(zip(xs, LEVELS)):
        r = 11
        if i < step: d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE)
        else: d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=PEACH, outline=MUTED, width=3)
        col = INK if i == step - 1 else MUTED
        f = font(28, 650 if i == step - 1 else 450)
        tw = d0.textlength(lv, font=f, features=FE)
        d.text((cx - tw / 2, cy + 44), lv, font=f, fill=col, anchor='ls', features=FE)
    y += lad_h + gap
    # hook
    d.rectangle((x0, y, x0 + BOXW, y + hook_h), fill=WHITE)
    for i, l in enumerate(hook_lines):
        by = y + 30 + 44 + i * hstep
        if '{E}' in l and hook_emoji:
            a, b = l.split('{E}'); e = emoji(hook_emoji, 44)
            wa = d0.textlength(a, font=fh, features=FE); wb = d0.textlength(b, font=fh, features=FE)
            tw = wa + 10 + e.width + 10 + wb; bx = x0 + (BOXW - tw) / 2
            d.text((bx, by), a, font=fh, fill=INK, anchor='ls', features=FE)
            im.alpha_composite(e, (int(bx + wa + 10), by - 40))
            d.text((bx + wa + 20 + e.width, by), b, font=fh, fill=INK, anchor='ls', features=FE)
        else:
            tw = d0.textlength(l, font=fh, features=FE); bx = x0 + (BOXW - tw) / 2
            d.text((bx, by), l, font=fh, fill=INK, anchor='ls', features=FE)
    y += hook_h + gap
    # text
    d.rectangle((x0, y, x0 + BOXW, y + text_h), fill=PEACH)
    for i, l in enumerate(text_lines):
        d.text((x0 + 38, y + 34 + 38 + i * tstep), l, font=ft, fill=INK, anchor='ls', features=FE)
    im.save(out_png)

if __name__ == '__main__':
    step, clip, start, dur, out = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    png = out.replace('.mp4', '_overlay.png')
    build(step, ["Bu A1 metnini sözlüksüz", "anladıysan yoruma {E} bırak"], "✅",
          ["Every morning, I make a cup of tea.", "I put it on the table.", "My cat sits next to it.",
           "She looks at me. I look at her.", "I go to the kitchen for a minute.", "I come back.",
           "My tea is on the floor…", "and my cat is very happy."], png)
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps=30,format=yuv420p[bg];"
          f"[bg][1:v]overlay=0:0,format=yuv420p[v]")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', start, '-t', dur, '-i', clip, '-loop', '1', '-i', png,
                    '-filter_complex', vf, '-map', '[v]', '-t', dur, '-c:v', 'libx264', '-preset', 'slow', '-crf', '24',
                    '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', out], check=True)
    print(out)
