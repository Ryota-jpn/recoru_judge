import mysql.connector
import sys

def user_select(host,user,password,database):
    try:
        # MySQLに接続
        conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )


        # カーソルを取得
        cursor = conn.cursor()

        # クエリ実行
        select_query = "SELECT CONTRACT_ID, EMAIL, PASSWORD FROM USERS;"
        cursor.execute(select_query)

        # 結果を取得
        users = cursor.fetchall()

        # 結果を表示
        for user in users:
            print(user)

        # 接続を閉じる
        cursor.close()
        conn.close()

        return users

    except Exception:
        sys.exit()