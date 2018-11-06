import tesseract as ocr

from PIL import Image


phrase = ocr.image_to_string(Image.open('imagejpeg.jpeg'), lang='por')
print(phrase)