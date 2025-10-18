import os
import cv2
import pytesseract
from PIL import Image

# --- absolute path ---
base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "images", "example_img.png")

img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"Image not found at: {image_path}")

# --- convert to PIL Image ---
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(img_rgb)

# --- OCR ---
text = pytesseract.image_to_string(pil_img)
print(text)

# --- save output ---
with open('img-output.txt', 'a', encoding='utf-8') as f:
    f.write(text + "\n")
