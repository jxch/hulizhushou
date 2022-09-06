import easyocr
import logging

reader = easyocr.Reader(['en', 'ch_sim'])


def get_text(img_bytes):
    result = reader.readtext(img_bytes)
    logging.info(f"read result: {result}")

    text_list = []
    for t in result:
        text_list.append(t[-2])

    logging.info(f"text list: {text_list}")
    return text_list


def get_stem(text_list):
    stem_index = None
    for index, text in enumerate(text_list):
        if text == '单选题' or text == '多选题':
            stem_index = index + 1
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
        if text == 'B':
            options['B'] = text_list[index + 1]
        if text == 'C':
            options['C'] = text_list[index + 1]
        if text == 'D' or text == '0' or text == 0:
            options['D'] = text_list[index + 1]
        if text == 'E':
            options['E'] = text_list[index + 1]

    return options


