# -*- encoding=utf8 -*-
__author__ = "xiche"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "xiche"

from airtest.core.api import *
import requests
import time
import pandas as pd
import re 

auto_setup(__file__)



from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

data_path = r'E:\work\hulizhushou\res\data-2022-第一季度三基理论知识点练习-题库.txt'
tmp_path = r'E:\work\hulizhushou\tmp\data.json'
all_question_list = []

f=None
try:
    f = open(data_path, encoding='utf-8')
except BaseException:
    f = open(data_path, encoding='gbk')
    
for index, line in enumerate(f.readlines()):
    questions_json = line.strip()
    if len(questions_json) > 0:
        questions_json = questions_json.replace("\"", "")
        questions_json = questions_json.replace("\'", "\"")
        questions_json = questions_json.replace("\\", "\\\\")

        file = open(tmp_path, 'w', encoding='utf-8')
        file.write(str(questions_json))
        file.close()

        df = pd.read_json(tmp_path, encoding="utf-8")
        for df_index, row in df.iterrows():
            rights = re.findall(r'正确答案：[A-Z,]*', row['right'])[0].strip('正确答案：').strip().split(',')
            all_question_list.append({
                'name': row['name'],
                'right_option': rights
            })
        
f.close()


def touch_options(r_option_list):
    for option in r_option_list:
        if option == 'A':
            touch(Template(r"tpl1663586100277.png", record_pos=(-0.443, -0.552), resolution=(1200, 2000)))

        if option == 'B':
            touch(Template(r"tpl1663586107362.png", record_pos=(-0.443, -0.478), resolution=(1200, 2000)))

        if option == 'C':
            touch(Template(r"tpl1663586113855.png", record_pos=(-0.441, -0.398), resolution=(1200, 2000)))

        if option == 'D':
            touch(Template(r"tpl1663586121027.png", record_pos=(-0.442, -0.323), resolution=(1200, 2000)))

        if option == 'E':
            touch(Template(r"tpl1663586129679.png", record_pos=(-0.443, -0.246), resolution=(1200, 2000)))
        

def button_text():    
    button = poco("android:id/content").offspring("android.widget.ScrollView")[0].offspring("android.view.ViewGroup")[-1].offspring("android.widget.TextView")[0]
    return button.get_text()


num = 500

while num > 0:
    num = num - 1
    
    if exists(Template(r"tpl1663582803666.png", record_pos=(0.448, -0.752), resolution=(1200, 2000))):
        touch(Template(r"tpl1663582813854.png", record_pos=(0.448, -0.752), resolution=(1200, 2000)))
    
        poco(text="开始答题").click()
    
    while exists(Template(r"tpl1663582860933.png", record_pos=(-0.44, -0.552), resolution=(1200, 2000))):
        sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
        texts = sv.offspring("android.widget.TextView")

        question = {}
        question['stem'] = texts[0].get_text()

        is_exists = False
        for q in all_question_list:
            if q['name'] == question['stem']:
                touch_options(q['right_option'])
                is_exists = True
                break

        if not is_exists:
            raise Exception("题库里面没有这道题")
            
        if button_text() == "确定":
            poco(text="确定").click()
        if button_text() == "下一题":
            poco(text="下一题").click()
        elif exists(Template(r"tpl1679758259975.png", record_pos=(-0.002, 0.023), resolution=(1200, 2000))):
            touch(Template(r"tpl1679758278500.png", record_pos=(-0.003, 0.025), resolution=(1200, 2000)))
        if button_text() == "提 交" or exists(Template(r"tpl1679759883274.png", record_pos=(-0.001, -0.089), resolution=(1200, 2000))):
            poco(text="提 交").click()
            if exists(Template(r"tpl1673871798298.png", record_pos=(-0.23, -0.007), resolution=(1200, 2000))):
                touch(Template(r"tpl1663591654765.png", record_pos=(0.296, 0.07), resolution=(1200, 2000)))
                time.sleep(1)









    
    


