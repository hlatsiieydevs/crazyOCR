# OCR Overclocked
This is simply a mini project that I am working on that aims to digitise scanned documents into text files effectively and efficiently.

## Prerequisites
A system with Ubuntu
Anaconda
GPU drivers
Jupyter Notebook

## Setup
Install system packages
``` bash
sudo apt update
sudo apt install -y build-essential pkg-config \
    tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd tesseract-ocr-script-latn \
    poppler-utils
```

Verify Tesseract
``` bash
tesseract --version
tesseract --list-langs
```

If `eng`(and `Latin` or `script-latn`) appears, you're all good homie. If not, install the missing language packages.

