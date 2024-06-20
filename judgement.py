from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time
import chromedriver_binary
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()
URL = os.environ['URL']
CONTRACT_ID = os.environ['CONTRACT_ID']
AUTH_ID = os.environ['AUTH_ID']
PASSWORD = os.environ['PASSWORD']

# ブラウザの起動
driver = webdriver.Chrome()

# URL先に移動
driver.get(URL)

time.sleep(1)

# 各種入力フォームを取得
contract_id = driver.find_element(By.NAME, "contractId")  # 契約ID
auth_id = driver.find_element(By.NAME, "authId")  # ログインIDまたはメールアドレス
password = driver.find_element(By.NAME, "password")  # パスワード
submit = driver.find_element(By.CLASS_NAME, "common-btn")  # ログインボタン

# 入力フォームを空にする
contract_id.clear()
auth_id.clear()
password.clear()

# 各種入力情報をセット
contract_id.send_keys(CONTRACT_ID)
auth_id.send_keys(AUTH_ID)
password.send_keys(PASSWORD)

# ログインボタンを押下
submit.click()

time.sleep(5)

# ブラウザを閉じる
driver.close()
