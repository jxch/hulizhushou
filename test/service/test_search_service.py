import service.search_service as search_service
import util.json_util as json_util
import core.ocr as ocr
import base64

right_text_list = search_service.get_right_text_list(
    "新生儿泪囊炎有时用力向下压迫泪囊或加压冲洗泪道时可使鼻泪管开口处残膜穿破,若仍不通畅")

res = search_service.match_right_options(right_text_list,
                                         {"A": "正确", "B": "错误", "C": "烟酒过度", "D": "粉尘或化学刺激",
                                          "E": "长期应用刺激性药物"})

print(res)

img_url = r'../../res/1.jpg'
with open(img_url, 'rb') as f:
    a = f.read()

a = base64.b64encode(a)
right = search_service.search_option_by_img_base64(a)

print(right)

hidden = search_service.hidden_encode(['A', 'B', 'C'])
print(hidden)

right_hidden = search_service.hidden_search_option_by_img_base64(a)
print(right_hidden)