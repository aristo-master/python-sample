from setting import setting
from logging import config, getLogger

config.dictConfig(setting.LOGGING)
logger = getLogger(__name__)

import json


def json_test():
    # JSON形式の文字列を定義
    json_param = '{"key": "param"}'

    # エラー発生 AttributeError: 'str' object has no attribute 'read'
    # json.load(json_param)

    # 正常
    json.loads(json_param)


if __name__ == '__main__':
    json_test()
