from pdf2image import convert_from_path
import pytesseract

filePath = r'PDFtoText\021-DO-YOU-WONDER-ABOUT-RAIN-SNOW-SLEET-AND-HAIL-Free-Childrens-Book-By-Monkey-Pen.pdf'

# Convert PDF to images
pages = convert_from_path(filePath)  # Poppler must be in PATH

# Open a new text file to save the output
with open("pdf-output.txt", "w", encoding="utf-8") as f:
    for page_number, page_image in enumerate(pages, start=1):
        text = pytesseract.image_to_string(page_image)

        # Write page header
        f.write(f"--- Page {page_number} ---\n")
        # Write the OCR text
        f.write(text + "\n")
        # Optional separator between pages
        f.write("="*40 + "\n\n")

print("✅ OCR text saved to output.txt")
