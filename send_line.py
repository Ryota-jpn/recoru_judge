import requests
import os

URL = os.environ['URL']

def send_line(user_result):
    msg = f"""
    勤務時間が超過しています。
    至急、RecoRuをご確認ください。
    {URL}
    """
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + user_result[3]}
    payload = {'message': msg}

    try:
        requests.post(url,headers=headers, params=payload)
        print('LINE通知しました。')
    except Exception:
        print("エラーが発生しました。")

