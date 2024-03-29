
def iter_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    try:
        with open(file_name, encoding='utf-8') as of:
            buf_gen = takewhile(lambda x: x, (of.read(buffer) for _ in repeat(None)))
            return sum(buf.count("\n") for buf in buf_gen)
    except BaseException:
        with open(file_name, encoding='gbk') as of:
            buf_gen = takewhile(lambda x: x, (of.read(buffer) for _ in repeat(None)))
            return sum(buf.count("\n") for buf in buf_gen)
