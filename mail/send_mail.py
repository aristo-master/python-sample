import logging
from logging import getLogger
import smtplib
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG)
logger = getLogger(__name__)
FROM_ADDRESS = 'from@gmail.com'
PASSWORD = 'pass'
TO_ADDRESS = 'to@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_mail():
    """
    メールを送信する。
    :return: None
    """
    #########
    # メール文章の構築
    ####
    # 本文
    msg = MIMEText("こんにちわ。アリストマスターです。")
    # タイトル
    msg['Subject'] = "ぽこんち"
    # SMTPサーバと接続
    smtpobj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    # パスワードの設定が無い場合は「認証無し」でメールを送る。
    if PASSWORD:
        smtpobj.login(FROM_ADDRESS, PASSWORD)
    # 送信実行
    smtpobj.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    logger.info("メールを送信しました")
    # クローズ
    smtpobj.close()


if __name__ == '__main__':
    logger.info("start")
    send_mail()
    logger.info("end")
