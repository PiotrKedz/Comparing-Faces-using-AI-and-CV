import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text(image):
    lang = "pol+eng"
    config = "--psm 11 --oem 3"
    img = cv.resize(image, (800, 600))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)[1]
    text = pytesseract.image_to_string(thresh, lang=lang, config=config)
    return text
