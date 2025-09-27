#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT_DIR = os.path.join(ROOT, "images")
os.makedirs(OUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 512, 1920
BG = (32, 32, 32, 255)
FG = (255, 255, 255, 255)

# Prefer DejaVuSans from bundled Ren'Py common
FONT_CANDIDATES = [
    os.path.join(ROOT, "..", "..", "renpy-8.4.1-sdk", "renpy", "common", "DejaVuSans.ttf"),
    
]

def load_font(size: int):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()

NAMES = [
    "fox",
    "ariel",
    "gerald",
    "computer",
    "carpet",
    "nicky",
    "acorn",
    "hidee",
]

def make_image(name: str):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    title = name.capitalize()
    # scale font to width
    font_size = 120
    font = load_font(font_size)
    tw, th = draw.textsize(title, font=font)
    while tw > WIDTH - 40 and font_size > 20:
        font_size -= 8
        font = load_font(font_size)
        tw, th = draw.textsize(title, font=font)
    draw.text(((WIDTH - tw) / 2, (HEIGHT - th) / 2), title, fill=FG, font=font)
    out_path = os.path.join(OUT_DIR, f"{name}.png")
    img.save(out_path)
    return out_path

def main():
    for n in NAMES:
        p = make_image(n)
        print("wrote", p)

if __name__ == "__main__":
    main()

