from pdf2image import convert_from_path  # Converts PDF pages to images
import pytesseract                       # Python wrapper for Tesseract OCR

# Path to the PDF file
filePath = r'PDFtoText\example_file.pdf'

# --- Convert PDF to images ---
# This will convert each page of the PDF into a PIL Image object
# Note: Poppler must be installed and its bin folder added to your PATH
pages = convert_from_path(filePath)

# --- Open a new text file to save the OCR output ---
# "w" mode overwrites the file if it already exists
# encoding="utf-8" ensures all characters are saved correctly
with open("pdf-output.txt", "w", encoding="utf-8") as f:
    # Loop through each page image
    for page_number, page_image in enumerate(pages, start=1):
        # Perform OCR on the current page
        text = pytesseract.image_to_string(page_image)

        # Write a page header to separate pages in the text file
        f.write(f"--- Page {page_number} ---\n")
        # Write the extracted text
        f.write(text + "\n")
        # Optional visual separator between pages
        f.write("="*40 + "\n\n")

# Inform the user that OCR output has been saved
print("OCR text saved to output.txt")
