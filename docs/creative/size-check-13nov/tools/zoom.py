import sys, os
from PIL import Image, ImageDraw
def zoom(src, dst, box, scale=1.0, minor=50, major=100, label=100):
    im = Image.open(src).convert("RGB").crop(box); x0, y0 = box[0], box[1]
    im = im.resize((int(im.width * scale), int(im.height * scale))); d = ImageDraw.Draw(im)
    for x in range((x0 // minor + 1) * minor, box[2], minor):
        X = (x - x0) * scale; d.line([(X, 0), (X, im.height)], fill=(255, 0, 0) if x % major == 0 else (255, 150, 150), width=1)
        if x % label == 0: d.text((X + 2, 2), str(x), fill="yellow")
    for y in range((y0 // minor + 1) * minor, box[3], minor):
        Y = (y - y0) * scale; d.line([(0, Y), (im.width, Y)], fill=(255, 0, 0) if y % major == 0 else (255, 150, 150), width=1)
        if y % label == 0: d.text((2, Y + 2), str(y), fill="yellow")
    im.save(dst, quality=85)
if __name__ == "__main__":
    a = sys.argv; zoom(a[1], a[2], tuple(int(v) for v in a[3].split(",")), float(a[4]), int(a[5]), int(a[6]), int(a[7]))
