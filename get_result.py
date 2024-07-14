from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time
import chromedriver_binary
import os
import datetime
from dotenv import load_dotenv
from datetime import timedelta
from selenium.common.exceptions import WebDriverException
import judge_time

URL = os.environ['URL']

def get_work_time(users):
    user_results = []
    for user in users:
    # URL先に移動
        try:
            # # ブラウザの起動
            driver = webdriver.Chrome()
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
            contract_id.send_keys(user[0])
            auth_id.send_keys(user[2])
            password.send_keys(user[3])

        # ログインボタンを押下
            submit.click()

            time.sleep(1)

        # 各種勤務時間を取得
            contents = driver.find_element(By.ID, "AC_SUMMARY_1")
            summary = contents.find_elements(By.CLASS_NAME, "h-attendanceChart-summary-flex-content")
            work_time = {}
            for s in summary:
                title = s.find_element(By.CLASS_NAME, "title").text
                colon = ':'
                value = s.find_element(By.CLASS_NAME, "data").text
                hours = int(value[:value.find(colon)])
                minutes = int(value[value.find(colon)+1:])
                times = hours * 60 + minutes
                work_time[title] = times

            driver.close()

            tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
            today = datetime.datetime.now(tokyo_tz).day

            if(today == 15):
                result = judge_time.judge_middle(work_time)
            else:
                result = judge_time.judge_end(work_time)

            user_result = (user[0],user[1],user[2],user[4],work_time['所定時間'],work_time['労働時間'],result)
            user_results.append(user_result)

        except WebDriverException:
            print('例外が発生しました。処理を中止します。')
            driver.close()
            continue

    return user_results