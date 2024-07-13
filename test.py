import mysql.connector


# MySQLに接続
conn = mysql.connector.connect(
    host="localhost",
    user="developer",
    password="developer",
    database="develop"
)

# カーソルを取得
cursor = conn.cursor()

# ここでデータベースへの操作を行う
# テーブル作成のクエリ
select_query = "SELECT CONTRACT_ID, EMAIL, PASSWORD FROM USERS;"

# クエリ実行
cursor.execute(select_query)

# 結果を取得
result = cursor.fetchall()

print(result)
# 結果を表示
for row in result:
    print(row)

# 接続を閉じる
cursor.close()
conn.close()
