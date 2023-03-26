from os.path import dirname, abspath
import pandas as pd


def tiku_factory(code=None):
    if code == "18":
        return "题库-18.xlsx"
    if code == "2022年度护理人员晋级考试":
        return "题库-2022年度护理人员晋级考试.xlsx"
    if code == "2022-第一季度三基理论知识点练习":
        return "题库-2022-第一季度三基理论知识点练习.xlsx"
    return "题库.xlsx"


def df_factory(tiku):
    base_dir = dirname(dirname(abspath(__file__)))
    excel_path = base_dir + f"/res/{tiku}"
    return pd.read_excel(excel_path, sheet_name='题库')


def search_text(text, tiku):
    if text:
        text = text.replace("0)", "")
        text = text.replace(")", "\)")
        text = text.replace("(", "\(")
        return df_factory(tiku).query(f'name.str.contains("{text}")')
    else:
        return pd.DataFrame([])


def get_right_text_list(stem, tiku):
    stem_df = search_text(stem, tiku)
    right_text_list = []
    for index, row in stem_df.iterrows():
        for text in row['right_option'].split(';\n'):
            right_text_list.append(text)
    return right_text_list


def match_right_options(right_text_list, stem_options):
    right_options = []
    for key, value in stem_options.items():
        for text in right_text_list:
            if value == text:
                right_options.append(key)
                break

    return right_options


def get_right_options_by_question(question, tiku):
    right_text_list = get_right_text_list(question['stem'], tiku)
    return match_right_options(right_text_list, question['options'])


def hidden_encode(right_options):
    hidden = '0x'
    for option in right_options:
        hidden = hidden + str(ord(option) - ord('A') + 1)
    return hidden.ljust(7, '0')
