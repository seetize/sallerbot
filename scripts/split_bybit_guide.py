from pathlib import Path
from PIL import Image


SOURCE = Path("assets/bybit/bybit-guide.png")
OUT = SOURCE.parent

# Layout of the supplied 572x1014 portrait guide: two columns and three rows.
BOXES = {
    1: (18, 112, 282, 432),
    2: (298, 112, 560, 432),
    3: (18, 442, 282, 738),
    4: (298, 442, 560, 738),
    5: (18, 746, 282, 982),
    6: (298, 746, 560, 982),
}


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source image not found: {SOURCE}")
    with Image.open(SOURCE) as image:
        for step, box in BOXES.items():
            crop = image.crop(box)
            crop.save(OUT / f"bybit-step-{step}.png")
    print(f"Created {len(BOXES)} step images in {OUT}")


if __name__ == "__main__":
    main()
