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

# DB内のユーザー情報を取得
users = mysql_conn.user_select()

# ユーザーごとの残業時間の判定を取得
user_results = get_result.get_work_time(users)

for user_result in user_results:
    if(user_result[6]):
        send_mail.send_email(user_result)

print(user_results)
# [('170096', '木名瀬凌太', 'kinase.ryota@alhinc.jp', 10560, 5280.0, 4890, False)]

mysql_conn.results_insert(user_results)