import os
import datetime

URL = os.environ['URL']
tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
today = datetime.datetime.now(tokyo_tz).day

def make_html(user_result):
    if(today == 15):
        html = f"""
            <html><meta charset="utf-8">
                <body>
                    <h1 style="color:#ff0000">今月の残業時間が超過しています‼</h1>
                    <p>今月の所定労働時間が{user_result[4]/60}時間に対して、既に{user_result[5]/60}時間働いています。</p>
                    <p>このペースで働きますと、*月45時間以上の残業が発生する見込みです。(*36協定)</p>
                    <p>以下対応をお願いいたします</p>
                    <ul>
                        <li>RecoRuをご確認下さい。</li>
                        <li>残りの業務を調整して下さい。</li>
                        <li>難しい場合は、早めに上司に相談して下さい。</li>
                    </ul>
                    <a href={URL}>RecoRuはこちら</a>
                </body>
            </html>
        """
    else:
        html = f"""
            <html><meta charset="utf-8">
                <body>
                    <h1 style="color:#ff0000">今月の残業時間が超過しています‼</h1>
                    <p>今月の所定労働時間が{user_result[4]/60}時間に対して、{user_result[5]/60}時間働いています。</p>
                    <p>*月45時間以上の残業が発生しています。(*36協定)</p>
                    <p>以下対応をお願いいたします</p>
                    <ul>
                        <li>RecoRuをご確認下さい。</li>
                        <li>来月の業務を調整して下さい。</li>
                        <li>難しい場合は、早めに上司に相談して下さい。</li>
                    </ul>
                    <a href={URL}>RecoRuはこちら</a>
                </body>
            </html>
        """
    return html