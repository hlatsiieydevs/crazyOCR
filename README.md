# OCR Overclocked
This is simply a mini project that I am working on that aims to digitise scanned documents into text files effectively and efficiently.

## Prerequisites
A system with Ubuntu
Anaconda
GPU drivers
Jupyter Notebook

## Setup
### Install required packages
Update local repository
``` bash
sudo apt update
```

Install required packages
``` bash
sudo apt install -y build-essential pkg-config \
    tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd tesseract-ocr-script-latn \
    poppler-utils
```

### Verify Tesseract
Confirm Tesseract is installed
``` bash
tesseract --version
```

Confirm the required Tesseract packages are installed
``` bash
tesseract --list-langs
```
If `eng`(and `Latin` or `script-latn`) appears, you're all good homie. If not, install the missing language packages.

### Launch into your Conda environment 
If you have used Jupyter Notebook, try using the Conda Environment you used when using Jupyter.
How can you find the name of the environment if forgotten? You may wonder. Don't worry.

Just type
``` bash
conda info --envs
```

The names should pop up.

Launch into the environment
``` bash
conda activate <name-of-environment>
```

### Install necessary packages in the environment

``` bash
conda install -c conda-forge numpy pillow matplotlib scikit-image pandas jupyterlab notebook ipywidgets opencv pytesseract -y
```

Transformers / TrOCR (neural OCR)
```bash
pip install transformers accelerate bitsandbytes sentencepiece easyocr
```
