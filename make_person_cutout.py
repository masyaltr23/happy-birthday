from rembg import remove, new_session
from PIL import Image

src = r"WhatsApp Image 2026-09-27 at 16.46.53.jpeg"
out = r"img/person_cutout.png"
img = Image.open(src).convert("RGBA")
session = new_session(model_name="u2netp")
cutout = remove(img, session=session)
cutout.save(out)
print(f"saved {out} size={cutout.size}")
