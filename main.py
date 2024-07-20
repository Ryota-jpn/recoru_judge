from dotenv import load_dotenv
import mysql_conn
import get_result
import send_mail
import send_line

def main(evebt, context):
    print('処理を開始します。')

    # 環境変数を読み込む
    load_dotenv()

    # DB内のユーザー情報を取得
    users = mysql_conn.user_select()

    # ユーザーごとの残業時間の判定を取得
    user_results = get_result.get_work_time(users)

    # user_results = (ID,氏名,メールアドレス,LINEアカウント,所定労働時間,実労働時間,判定結果)

    # 残業時間が超過しているUSERのみメール通知
    for user_result in user_results:
        if(user_result[6]):
            send_mail.send_email(user_result)
            send_line.send_line(user_result)

    # USERごとの労働時間の判定結果をINSERT
    mysql_conn.results_insert(user_results)

    print('処理が終了しました。')