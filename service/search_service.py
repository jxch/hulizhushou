from os.path import dirname, abspath

import pandas as pd

base_dir = dirname(dirname(abspath(__file__)))
excel_path = base_dir + "/res/题库.xlsx"
df = pd.read_excel(excel_path, sheet_name='题库')


def search_text(text):
    return df.query(f'name.str.contains("{text}")')
