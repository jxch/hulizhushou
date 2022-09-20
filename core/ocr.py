import easyocr
import logging
from functools import lru_cache


@lru_cache(maxsize=1)
def get_reader():
    return easyocr.Reader(['en', 'ch_sim'], gpu=True)


def init_ocr():
    get_reader()


def get_text(img_bytes):
    reader = get_reader()
    result = reader.readtext(img_bytes)
    logging.info(f"read result: {result}")

    text_list = []
    for t in result:
        text_list.append(t[-2])

    return text_list


def get_stem(text_list):
    stem_index = None
    for index, text in enumerate(text_list):
        if text == '考生:马文静 (日间)' or text == '考生:马文静(日间)':
            stem_index = index + 2
            break

    if stem_index is not None:
        return text_list[stem_index]
    else:
        return None


def get_options(text_list):
    options = {}
    for index, text in enumerate(text_list):
        if text == 'A':
            options['A'] = text_list[index + 1]
        if text == 'B' or text == '8' or text == 8:
            options['B'] = text_list[index + 1]
            if '错误' == options['B']:
                break
        if text == 'C' or text == '6' or text == 6:
            options['C'] = text_list[index + 1]
        if text == 'D' or text == '0' or text == 0:
            options['D'] = text_list[index + 1]
        if text == 'E' or text == '巳':
            options['E'] = text_list[index + 1]
            break

    return options
