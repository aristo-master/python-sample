"""
HTTPリクエストのGet通信のサンプルです。
"""

import urllib.request
import urllib.parse
from setting import setting
from logging import config, getLogger

config.dictConfig(setting.LOGGING)
logger = getLogger(__name__)

# 正常なURL
UZU_BLOG_FEED_URL = 'https://blog.uzumax.org/feeds/posts/summary?published-min=2018-05-31T00:00:00&published-max=2018-07-01T23:59:59&orderby=published&max-results=500'

# 存在しないURL
NOT_FOUNT_URL = 'https://xxx.uzumax.org/'


def http_get(target_url):
    """
    正常に処理が完了するリクエストを送信します。

    Args:
        target_url (str): 送信先URL
    """
    logger.info('送信先URL=%s', target_url)

    try:

        # target_urlに向けて接続する。
        with urllib.request.urlopen(target_url) as res:

            # レスポンスを受け取る。
            # 人間が読み取る為にはデコードが必要。
            body = res.read().decode("utf-8")

            logger.info(body)

    except urllib.error.URLError as e:

        logger.exception("リクエストに失敗しました。ＵＲＬが不正です。", e)


    except Exception as e:

        logger.exception("リクエストに失敗しました。", e)


if __name__ == '__main__':
    # 正常に通信出来る処理
    http_get(UZU_BLOG_FEED_URL)
    # ＵＲＬが存在しない処理
    http_get(NOT_FOUNT_URL)
