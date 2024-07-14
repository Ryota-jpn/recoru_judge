import mysql.connector
import sys
import os
import datetime


HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']

# USER情報のSELECT
def user_select():
    try:
        # MySQLに接続
        conn = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )


        # カーソルを取得
        cursor = conn.cursor()

        # クエリ実行
        select_query = "SELECT CONTRACT_ID, NAME, EMAIL, PASSWORD, LINE_ACC FROM USERS;"
        cursor.execute(select_query)

        # 結果を取得
        users = cursor.fetchall()

        # 接続を閉じる
        cursor.close()
        conn.close()

        print("SELECTしました")

        return users

    except Exception:
        # 接続を閉じる
        cursor.close()
        conn.close()
        sys.exit()

# 労働時間の判定結果をINSERT
def results_insert(user_results):
    tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
    dt = datetime.datetime.now(tokyo_tz)
    year = dt.year
    month = dt.month
    if(dt.day == 15):
        category = "Middle"
    else:
        category = "End"

    try:
        # MySQLに接続
        conn = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )

        # カーソルを取得
        cursor = conn.cursor()

        # クエリ実行
        insert_query = """
            INSERT INTO RESULTS (
                CONTRACT_ID,
                NAME,
                YEAR,
                MONTH,
                CATEGORY,
                SCHEDULED_WORKING_HOURS,
                WORKING_HOURS,
                JUDGE)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        for result in user_results:
            if(result[6]):
                judge = "NG"
            else:
                judge = "OK"

            data = (result[0],result[1],year,month,category,result[4]/60,result[5]/60,judge)
            cursor.execute(insert_query,data)

        conn.commit()

        # 接続を閉じる
        cursor.close()
        conn.close()

        print("INSERTしました")

    except Exception:
        # 接続を閉じる
        cursor.close()
        conn.close()
        sys.exit()