# OCR.py
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def OCR(image):
    pytesseract.pytesseract.tesseract_cmd = 'Lib/site-packages/pytesseract/tesseract/tesseract'

    im = Image.open(image) # Ouverture du fichier image

    # Filtrage (augmentation du contraste)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')

    # Lancement de la procédure de reconnaissance
    text = pytesseract.image_to_string(im)
    print(text)