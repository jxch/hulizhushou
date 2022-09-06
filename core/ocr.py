import easyocr
import logging

reader = easyocr.Reader(['en', 'ch_sim'])


def get_text(img_bytes):
    result = reader.readtext(img_bytes)
    logging.info(f"read text result: {result}")
    text_lis = []
    for t in result:
        text_lis.append(t[-2])

    logging.info(f"read text result: {text_lis}")

    return None
