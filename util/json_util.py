import functools
import json
import logging
from pandas import DataFrame
from datetime import datetime, date


def json_dumps_default_date(obj, fmt='%Y-%m-%d'):
    if isinstance(obj, datetime):
        return obj.strftime(fmt)
    elif isinstance(obj, date):
        return obj.strftime(fmt)
    else:
        return obj


def return_json(func, json_date_fmt_func=json_dumps_default_date, indent=None):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        res = func(*args, **kw)
        if type(res) is str:
            return res
        if type(res) is dict or type(res) is list:
            return json.dumps(res, indent=indent, ensure_ascii=False, default=json_date_fmt_func)
        if type(res) is DataFrame:
            return json.dumps(res.to_dict('records'), indent=indent, ensure_ascii=False, default=json_date_fmt_func)
        logging.info("不支持的转JSON类型")
        return res

    return wrapper


@return_json
def to_json(data):
    return data
