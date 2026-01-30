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

data_path = r'D:\hulizhushou\res\data-2025-第四季度三基理论-题库.txt'
s_question_list = []
all_question_list = []
    
def touch_options(r_option_list):
    sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
    texts = sv.offspring("android.widget.TextView")
    for option in r_option_list:
        if option == 'A':
            texts[0 * 3 + 4 + 1].click();
        if option == 'B':
            texts[1 * 3 + 4 + 1].click();
        if option == 'C':
            texts[2 * 3 + 4 + 1].click();
        if option == 'D':
            texts[3 * 3 + 4 + 1].click();
        if option == 'E':
            texts[4 * 3 + 4 + 1].click();
        if option == 'F':
            texts[5 * 3 + 4 + 1].click();

def right_options(right_text):
    return right_text.split("你的答案：")[0].strip("正确答案：").strip().split(",")


def button_text():    
    button = poco("android:id/content").offspring("android.widget.ScrollView")[0].offspring("android.view.ViewGroup")[-1].offspring("android.widget.TextView")[0]
    return button.get_text()



try: 
    num = 30000

    while num > 0:
        num = num - 1

        if exists(Template(r"tpl1766305407954.png", record_pos=(0.426, -0.952), resolution=(1080, 2340))):
            touch(Template(r"tpl1766305407954.png", record_pos=(0.426, -0.952), resolution=(1080, 2340)))
            time.sleep(2)
            if exists(Template(r"tpl1766305487729.png", record_pos=(0.012, 0.95), resolution=(1080, 2340))):
                touch(Template(r"tpl1766305487729.png", record_pos=(0.012, 0.95), resolution=(1080, 2340)))
                time.sleep(1)
            if exists(Template(r"tpl1766307467959.png", record_pos=(0.131, 0.945), resolution=(1080, 2340))):
                touch(Template(r"tpl1766307467959.png", record_pos=(0.131, 0.945), resolution=(1080, 2340)))
                time.sleep(1)
        time.sleep(1)
        while exists(Template(r"tpl1766378350872.png", record_pos=(-0.416, -0.519), resolution=(1080, 2340))) :


            sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
            texts = sv.offspring("android.widget.TextView")

            question = {}
            question['num'] = texts[2].get_text()
            question['stem'] = texts[3].get_text()
            question['options'] = {}

            for i in range(0, int((len(texts) - 4 - 1) / 3)):
                question['options'][texts[i * 3 + 4 + 1].get_text()] = texts[i * 3 + 4 + 2].get_text()
            
            print(question['options'])
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
                touch(Template(r"tpl1766305508276.png", record_pos=(-0.413, -0.516), resolution=(1080, 2340)))



                if button_text() == "确定":
                    poco(text="确定").click()
                data_sv = poco("android:id/content").offspring("android.widget.ScrollView")[0]
                data_texts = texts = sv.offspring("android.widget.TextView")
                data_question = {}
                data_question['num'] = data_texts[2].get_text()
                data_question['name'] = data_texts[3].get_text()
                data_question['right'] = data_texts[-5].get_text()
                index = -5
                while "正确答案" not in data_question['right'] :
                    index = index + 1
                    data_question['right'] = data_texts[index].get_text()
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

                time.sleep(1)
                if exists(Template(r"tpl1673871798298.png", record_pos=(-0.23, -0.007), resolution=(1200, 2000))):
                    touch(Template(r"tpl1663591654765.png", record_pos=(0.296, 0.07), resolution=(1200, 2000)))
                    time.sleep(2)
                if exists(Template(r"tpl1766306382755.png", record_pos=(0.003, 0.006), resolution=(1080, 2340))):
                    touch(Template(r"tpl1766306393978.png", record_pos=(0.328, 0.085), resolution=(1080, 2340)))
                    time.sleep(2)
        time.sleep(2)


except BaseException as e:
    print(e)
    traceback.print_exc()            
    print("代码bug，保存的题：")
    print('all_question_list::')
    print(repr(all_question_list))
    print('s_question_list::')
    print(repr(s_question_list))








    
    



