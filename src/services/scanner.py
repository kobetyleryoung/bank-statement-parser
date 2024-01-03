import os
import re
import shutil
import numpy as np
import pandas as pd
import pytesseract
import pdf2image
from tabula import read_pdf

def get_pattern(*args) -> list:
    """
    Get pattern for matching
    """
    PDF_PATTERN = [
        re.compile(rf'{arg}', re.IGNORECASE) for arg in args
    ]
    
    return PDF_PATTERN

def split_statement(self) -> None:
    """
    Split statement into pages
    """
    #Convert pdf to image
    pages = pdf2image.convert_from_path(self.path, dpi=300)

    #Save images
    for i, page in enumerate(pages):
        page.save(f'{self.path[:-4]}_{i}.pdf', 'PDF')
        
def extract_text(self) -> None:
    """
    Extract text from pdf
    """
    #Convert pdf to image
    pages = pdf2image.convert_from_path(self.path, dpi=300)

    #Extract text
    text = []
    for page in pages:
        text.append(pytesseract.image_to_string(page))

    #Save text
    with open(f'{self.path[:-4]}.txt', 'w') as f:
        f.write('\n\n'.join(text))