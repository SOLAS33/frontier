"""Shrinks the downloaded photos for the web: max 1600px wide, JPEG quality 74, progressive. Prints before and after sizes,
and writes a contact sheet (sheet.jpg) so a human can check what each picture actually shows."""
from pathlib import Path

from PIL import Image, ImageDraw

IMG = Path(__file__).resolve().parents[1] / "frontier" / "assets" / "img"


def main():
    files = sorted(p for p in IMG.glob("*.jpg") if p.name != "sheet.jpg")
    thumbs = []
    for p in files:
        im = Image.open(p).convert("RGB")
        before = p.stat().st_size
        if before < 420_000 and im.width <= 1600:
            t = im.copy(); t.thumbnail((360, 240)); thumbs.append((p.name, t)); continue
        if im.width > 1600:
            im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        im.save(p, "JPEG", quality=74, optimize=True, progressive=True)
        print(f"{p.name:22s} {before // 1024:5d} KB -> {p.stat().st_size // 1024:4d} KB  {im.width}x{im.height}")
        t = im.copy()
        t.thumbnail((360, 240))
        thumbs.append((p.name, t))
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 370, rows * 270), "white")
    d = ImageDraw.Draw(sheet)
    for i, (n, t) in enumerate(thumbs):
        x, y = (i % cols) * 370 + 5, (i // cols) * 270 + 5
        sheet.paste(t, (x, y))
        d.text((x, y + 245), n, fill="black")
    sheet.save(IMG / "sheet.jpg", quality=80)


if __name__ == "__main__":
    main()
