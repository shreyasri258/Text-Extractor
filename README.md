# Text Extractor OCR with Python (pytesseract + pdf2image)

A simple Python tool to extract text from PDFs or images using OCR (Optical Character Recognition) and save it to a text file.

This project uses:

* pytesseract – Python wrapper for Tesseract OCR
* pdf2image – Convert PDF pages to images
* Poppler – PDF rendering library used by pdf2image
* OpenCV (optional) – For image preprocessing

## Features

* Convert PDFs to images and extract text from each page.
* Extract text from images (.png, .jpg).
* Save all extracted text into a single output.txt file.
* Handles multiple pages, with page separation in the output file.

## Prerequisites

### 1. Python

Make sure you have Python 3.10+ installed. Check version:

```bash
python --version
```

### 2. Install required Python packages

```bash
pip install pytesseract pdf2image pillow opencv-python
```

### 3. Install Tesseract OCR

* Download Tesseract OCR from [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki) (Windows installer).
* Default installation path: C:\Program Files\Tesseract-OCR\tesseract.exe
* Add Tesseract to system PATH (optional) or set its path explicitly in your code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

* Test installation:

```bash
tesseract --version
```

### 4. Install Poppler (for PDF conversion)

* Download Poppler for Windows: [http://blog.alivate.com.au/poppler-windows/](http://blog.alivate.com.au/poppler-windows/)
* Extract to a folder, e.g.: C:\Program Files\poppler-25.07.0
* Add the bin folder to PATH: C:\Program Files\poppler-25.07.0\Library\bin
* Or pass path explicitly in code:

```python
pages = convert_from_path(filePath, poppler_path=r"C:\Program Files\poppler-25.07.0\Library\bin")
```

## Project Structure

```
Text-Extractor-OCR-Pytessaract/
│
├─ images/                 # Store input images here
│   └─ sample.png
├─ PDFtoText/              # Store input PDFs here
│   └─ book.pdf
├─ BasicOcr.py             # Simple image OCR example
├─ pdf2text.py             # PDF to text example
└─ README.md               # This documentation
```

## Usage

### 1. Extract text from an image

```python
import cv2
import pytesseract

img = cv2.imread("images/sample.png")
text = pytesseract.image_to_string(img)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("OCR text saved to output.txt")
```

### 2. Extract text from a PDF

```python
from pdf2image import convert_from_path
import pytesseract

filePath = r"PDFtoText/book.pdf"

# Convert PDF pages to images (poppler_path optional)
pages = convert_from_path(filePath, poppler_path=r"C:\Program Files\poppler-25.07.0\Library\bin")

with open("output.txt", "w", encoding="utf-8") as f:
    for page_number, page_image in enumerate(pages, start=1):
        text = pytesseract.image_to_string(page_image)
        f.write(f"--- Page {page_number} ---\n{text}\n\n")

print("OCR text saved to output.txt")
```

## Tips for Better OCR

* If text quality is poor, consider preprocessing images:

```python
import cv2

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 85, 11)
text = pytesseract.image_to_string(thresh)
```

* Use PDFs with 300 DPI or higher for more accurate OCR.

## Troubleshooting

| Issue                          | Fix                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| PDFPageCountError              | Check PDF path, use absolute path, ensure Poppler is installed and in PATH             |
| TesseractNotFoundError         | Ensure Tesseract is installed and path is set in pytesseract.pytesseract.tesseract_cmd |
| Unicode characters not showing | Save text file with encoding="utf-8"                                                   |
| Image not found                | Make sure image file exists and path is correct                                        |

## License

This project is open source and free to use.
