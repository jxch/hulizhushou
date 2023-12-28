# -*- encoding=utf8 -*-
__author__ = "xiche"

from airtest.core.api import *
import requests
import time
import traceback

auto_setup(__file__)



from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

data_path = r'D:\hulizhushou\res\data-2023-第四季度三基理论-题库.txt'
s_question_list = []
all_question_list = []


def touch_options(r_option_list):
    for option in r_option_list:
        if option == 'A':
            touch(Template(r"tpl1695695758291.png", record_pos=(-0.442, -0.477), resolution=(1200, 2000)))
                    
        if option == 'B':
            touch(Template(r"tpl1695695770262.png", record_pos=(-0.443, -0.4), resolution=(1200, 2000)))

        if option == 'C':
            touch(Template(r"tpl1695695783131.png", record_pos=(-0.44, -0.323), resolution=(1200, 2000)))

        if option == 'D':
            touch(Template(r"tpl1695695792582.png", record_pos=(-0.443, -0.244), resolution=(1200, 2000)))

        if option == 'E':
            touch(Template(r"tpl1695695801224.png", record_pos=(-0.442, -0.168), resolution=(1200, 2000))) 
        if option == 'F':
            touch(Template(r"tpl1698125702694.png", record_pos=(-0.466, 0.121), resolution=(2000, 1200)))




def right_options(right_text):
    return right_text.split("你的答案：")[0].strip("正确答案：").strip().split(",")


def button_text():    
    button = poco("android:id/content").offspring("android.widget.ScrollView")[0].offspring("android.view.ViewGroup")[-1].offspring("android.widget.TextView")[0]
    return button.get_text()



try: 
    num = 100

    while num > 0:
        num = num - 1

        if exists(Template(r"tpl1663582803666.png", record_pos=(0.448, -0.752), resolution=(1200, 2000))):
            touch(Template(r"tpl1663582813854.png", record_pos=(0.448, -0.752), resolution=(1200, 2000)))

            poco(text="开始答题").click()

        while exists(Template(r"tpl1663582860933.png", record_pos=(-0.44, -0.552), resolution=(1200, 2000))):
            sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
            texts = sv.offspring("android.widget.TextView")

            question = {}
            question['num'] = texts[2].get_text()
            question['stem'] = texts[3].get_text()
            question['options'] = {}


            for i in range(4, len(texts) - 1):
                question['options'][chr(i - 4 + ord('A'))] = texts[i].get_text()

    #         r = requests.post("http://127.0.0.1:5000/right_options", json={'question':question})
    #         r_options = r.json()

    #         if len(r_options) == 0:
            success = False
            for q in all_question_list:
                if q['name'] == question['stem']:
                    touch_options(right_options(q['right']))
                    success = True
                    print(f"----->>>>>>> {q['name']}: {q['right']} -> {right_options(q['right'])}")
                    break

            if success is False:
                touch(Template(r"tpl1663586201735.png", record_pos=(-0.44, -0.554), resolution=(1200, 2000)))
                if button_text() == "确定":
                    poco(text="确定").click()
                data_sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
                data_texts = texts = sv.offspring("android.widget.TextView")
                data_question = {}
                data_question['num'] = data_texts[2].get_text()
                data_question['name'] = data_texts[3].get_text()
                data_question['right'] = data_texts[-2].get_text()
                if "答案解析" in data_question['right'] :
                    data_question['right'] = data_texts[-4].get_text()
                data_question['option'] = question['options']
                s_question_list.append(data_question)
                all_question_list.append(data_question)
                print(data_question)

    #         else:
    #             touch_options(r_options)
            if button_text() == "确定":
                poco(text="确定").click()
            if button_text() == "下一题":
                poco(text="下一题").click()
            elif exists(Template(r"tpl1679758259975.png", record_pos=(-0.002, 0.023), resolution=(1200, 2000))):
                touch(Template(r"tpl1679758278500.png", record_pos=(-0.003, 0.025), resolution=(1200, 2000)))

            if button_text() == "提 交" or exists(Template(r"tpl1679759883274.png", record_pos=(-0.001, -0.089), resolution=(1200, 2000))):
                print("提交")
                if s_question_list:
                    print("写入")
                    try:
                        with open(data_path, "a", encoding='utf-8') as fp:
                            fp.write("\n")
                            fp.write(repr(s_question_list))
                            fp.write("\n")
                            s_question_list = []
                    except BaseException as e:
                        print(e)
                        traceback.print_exc()
                        print("写入错误，原题如下：")
                        print(repr(s_question_list))
                        s_question_list = []
                poco(text="提 交").click()

                time.sleep(0.5)
                if exists(Template(r"tpl1673871798298.png", record_pos=(-0.23, -0.007), resolution=(1200, 2000))):
                    touch(Template(r"tpl1663591654765.png", record_pos=(0.296, 0.07), resolution=(1200, 2000)))
                    time.sleep(1)
except BaseException as e:
    print(e)
    traceback.print_exc()            
    print("代码bug，保存的题：")
    print('all_question_list::')
    print(repr(all_question_list))
    print('s_question_list::')
    print(repr(s_question_list))








    
    


