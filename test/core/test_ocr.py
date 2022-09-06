import core.ocr as ocr
import base64
import logging
logging.basicConfig(level=logging.INFO)

img_url = r'../../res/1.jpg'
with open(img_url, 'rb') as f:
    a = f.read()

res = ocr.get_text(a)
