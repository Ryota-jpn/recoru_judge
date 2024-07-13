import smtplib, ssl
from email.mime.text import MIMEText
import os
import make_mail_msg

# 送信元のGmailアカウントの取得
GACCOUNT = os.environ['GACCOUNT']
GPASSWORD = os.environ['GPASSWORD']

# メイン
def send_email(user):
    send_address = user[1]
    html = make_mail_msg.make_html(user)
    msg = make_mime_text(
        mail_to = send_address,
        subject = "【重要】今月の労働時間について",
        body = html
    )
    send_gmail(msg)

# 件名、送信先アドレス、本文を渡す関数
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = GACCOUNT
    return msg

# smtp経由でメール送信する関数
def send_gmail(msg):
    try:
        server = smtplib.SMTP_SSL(
            "smtp.gmail.com", 465,
            context = ssl.create_default_context())
        server.set_debuglevel(0)
        server.login(GACCOUNT, GPASSWORD)
        server.send_message(msg)
        print("メールが送信できました。")
    except Exception:
        print("エラーが発生しました。")
