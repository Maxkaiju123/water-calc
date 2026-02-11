import base64
import re
from pathlib import Path

def extract_png():
    svg_path = Path('icons/MoZiS.svg')
    if not svg_path.exists():
        print("Error: MoZiS.svg not found")
        return

    content = svg_path.read_text(encoding='utf-8')
    # Match the base64 data inside the href attribute
    match = re.search(r'href="data:image/png;base64,([^"]+)"', content)
    if not match:
        print("Error: Could not find base64 image data in SVG")
        return

    b64_data = match.group(1)
    img_data = base64.b64decode(b64_data)

    Path('icons/icon-192.png').write_bytes(img_data)
    Path('icons/icon-512.png').write_bytes(img_data)
    print("Successfully created icons/icon-192.png and icons/icon-512.png")

if __name__ == "__main__":
    extract_png()
