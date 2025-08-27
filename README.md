# crazyOCR
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
sudo apt update && sudo apt upgrade
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
Create a Conda environment. Enter a name of your choosing.
``` bash
conda create -n <name-of-environment> python=3.10 -y
```

Launch into the environment
``` bash
conda activate <name-of-environment>
```

### Install necessary packages in the environment
``` bash
conda install -c conda-forge pytorch torchvision torchaudio nvidia pytorch-cuda opencv pillow matplotlib numpy pytesseract -y
```
