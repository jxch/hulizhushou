from os.path import dirname, abspath
import core.ocr as ocr
import pandas as pd
import base64

base_dir = dirname(dirname(abspath(__file__)))
excel_path = base_dir + "/res/题库.xlsx"
df = pd.read_excel(excel_path, sheet_name='题库')


def search_text(text):
    return df.query(f'name.str.contains("{text}")')


def get_right_text_list(stem):
    stem_df = search_text(stem)
    right_text_list = []
    for index, row in stem_df.iterrows():
        for text in row['right_option'].split(';\n'):
            right_text_list.append(text)
    return right_text_list


def match_right_options(right_text_list, stem_options):
    right_options = []
    for key, value in stem_options.items():
        for text in right_text_list:
            if value in text:
                right_options.append(key)
                break

    return right_options


def search_option_by_img_base64(img_base64):
    img = base64.b64decode(img_base64)
    text_list = ocr.get_text(img)
    stem = ocr.get_stem(text_list)
    options = ocr.get_options(text_list)
    right_text_list = get_right_text_list(stem)
    right_options = match_right_options(right_text_list, options)
    return right_options


def hidden_encode(right_options):
    hidden = '0x'
    for option in right_options:
        hidden = hidden + str(ord(option) - ord('A') + 1)
    return hidden.ljust(7, '0')


def hidden_search_option_by_img_base64(img_base64):
    right_options = search_option_by_img_base64(img_base64)
    return hidden_encode(right_options)
