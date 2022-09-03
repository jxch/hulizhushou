import pandas as pd
import re
from core.utils import iter_count

data_path = "../res/data.txt"
tmp_path = "../tmp/data.json"
excel_path = "../res/题库.xlsx"

all_q = []

lines_num = iter_count(data_path)
f = open(data_path, encoding='gbk')
for index, line in enumerate(f.readlines()):
    print('\r', "lines:" + str(index + 1) + "/" + str(lines_num), end='', flush=True)
    questions_json = line.strip()
    if len(questions_json) > 0:
        questions_json = questions_json.replace("\'", "\"")

        file = open(tmp_path, 'w')
        file.write(str(questions_json))
        file.close()

        df = pd.read_json(tmp_path, encoding="gbk")

        for df_index, row in df.iterrows():
            rights = re.findall(r'正确答案：[A-Z,]*', row['right'])[0].strip('正确答案：').strip().split(',')
            all_q.append({
                'name': row['name'],
                'all_option': ";\n".join(list(row['option'].values())),
                'right_option': ";\n".join([row['option'][r] for r in rights])
            })

# 去重 & 排序
lis = [dict(t) for t in set([tuple(d.items()) for d in all_q])]
lis = sorted(lis, key=lambda i: (i['name']))

# 写入文件
pf = pd.DataFrame(list(lis))
pf.to_excel(excel_path, sheet_name='题库', encoding='gbk', index=False)

print('\nSUCCESS')
