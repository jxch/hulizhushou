import service.search_service as search_service
import util.json_util as json_util

res = search_service.search_text("")
res = json_util.to_json(res)
print(res)