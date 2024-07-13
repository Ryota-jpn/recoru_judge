import os
from dotenv import load_dotenv
import mysql_conn
import get_result
import send_mail
import smtplib, ssl
from email.mime.text import MIMEText
#上で作成したpyファイルから、account情報を読み込みます

# 環境変数を読み込む
load_dotenv()
URL = os.environ['URL']
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']

# DB内のユーザー情報を取得
users = mysql_conn.user_select(HOST, USER, PASSWORD, DATABASE)

# ユーザーごとの残業時間の判定を取得
user_results = get_result.get_work_time(URL,users)

for user in user_results:
    if(user[6]):
        print('TRUE')
    else:
        send_mail.send_email(user)

print(user_results)