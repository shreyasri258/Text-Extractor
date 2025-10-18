import os                  # For handling file paths and interacting with the OS
import cv2                 # OpenCV library for image processing
import pytesseract         # Python wrapper for Tesseract OCR
from PIL import Image      # Pillow library to work with images in a format Tesseract expects

# --- absolute path ---
# Get the directory where this script is located
base_path = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the image file
image_path = os.path.join(base_path, "images", "example_img.png")

# Read the image using OpenCV
img = cv2.imread(image_path)
# If the image cannot be read (wrong path, missing file, or corrupted image), raise an error
if img is None:
    raise FileNotFoundError(f"Image not found at: {image_path}")

# --- convert to PIL Image ---
# Convert OpenCV's BGR image to RGB (Tesseract expects RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Convert the NumPy array (OpenCV image) into a PIL Image for Tesseract
pil_img = Image.fromarray(img_rgb)

# --- OCR ---
# Run Tesseract OCR on the image and get the extracted text
text = pytesseract.image_to_string(pil_img)
# Print the extracted text to the console
print(text)

# --- save output ---
# Open (or create) a text file in append mode and write the OCR text
with open('img-output.txt', 'a', encoding='utf-8') as f:
    f.write(text + "\n")
