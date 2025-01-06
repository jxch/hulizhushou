from os.path import dirname, abspath
import pandas as pd
from pypinyin import lazy_pinyin

tiku_map_lazy = {}


def tiku_factory(code=None):
    if code == "2024-年终":
        return "题库-2024-年终.xlsx"
    if code == "2024-N3":
        return "题库-2024-N3.xlsx"
    if code == "2024-第三季度":
        return "题库-2024-第三季度.xlsx"
    if code == "2024-血糖":
        return "题库-2024-血糖.xlsx"
    if code == "2024-第一季度":
        return "题库-2024-第一季度.xlsx"
    if code == "2023-第二季度三基理论知识点练习":
        return "题库-2023-第二季度三基理论知识点练习.xlsx"
    if code == "18":
        return "题库-18.xlsx"
    if code == "2022年度护理人员晋级考试":
        return "题库-2022年度护理人员晋级考试.xlsx"
    if code == "2022-第一季度三基理论知识点练习":
        return "题库-2022-第一季度三基理论知识点练习.xlsx"
    if code == "2023-护理年终理论考核":
        return "题库-2023-护理年终理论考核.xlsx"
    if code == "2023-第四季度三基理论":
        return "题库-2023-第四季度三基理论.xlsx"
    return "题库.xlsx"


def convert_lazy_pinyin_str(name):
    return ''.join(lazy_pinyin(name))


def df_factory(tiku):
    if tiku not in tiku_map_lazy:
        base_dir = dirname(dirname(abspath(__file__)))
        excel_path = base_dir + f"/res/{tiku}"
        df = pd.read_excel(excel_path, sheet_name='题库')
        df['name_pinyin'] = df.apply(convert_lazy_pinyin_str, axis=1)
        tiku_map_lazy[tiku] = df
    return tiku_map_lazy[tiku]


def search_text(text, tiku):
    if text:
        text = text.replace("0)", "")
        text = text.replace(")", "\)")
        text = text.replace("(", "\(")
        return df_factory(tiku).query(
            f'name.str.contains("{text}") or name_pinyin.str.contains("{convert_lazy_pinyin_str(text)}")')
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
