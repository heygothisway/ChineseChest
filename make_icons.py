"""Generate PWA icons into ./icons (requires Pillow and a CJK font)."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'icons')
FONTS = [r'C:\Windows\Fonts\msjhbd.ttc', r'C:\Windows\Fonts\msjh.ttc', r'C:\Windows\Fonts\msyh.ttc']


def font(size):
    for f in FONTS:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def make(size, maskable):
    img = Image.new('RGBA', (size, size), (140, 88, 40, 255))
    d = ImageDraw.Draw(img)
    # Maskable icons keep content inside the central safe zone.
    r = size * (0.32 if maskable else 0.42)
    c = size / 2
    d.ellipse([c - r, c - r, c + r, c + r], fill=(253, 245, 230, 255), outline=(200, 150, 86, 255), width=max(2, size // 40))
    ri = r * 0.84
    d.ellipse([c - ri, c - ri, c + ri, c + ri], outline=(200, 30, 30, 255), width=max(2, size // 64))
    d.text((c, c), '帥', font=font(int(r * 1.15)), fill=(200, 30, 30, 255), anchor='mm')
    return img


os.makedirs(OUT, exist_ok=True)
for s in (192, 512):
    make(s, False).save(os.path.join(OUT, f'icon-{s}.png'))
    make(s, True).save(os.path.join(OUT, f'maskable-{s}.png'))
