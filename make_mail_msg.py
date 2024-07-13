def make_html(user_result):
    html = f"""
        <html><meta charset="utf-8">
            <body>
                <h1 style="color:#ff0000">今月の残業時間が超過しています‼</h1>
                <p>今月の所定労働時間が{user_result[3]/60}時間に対して、既に{user_result[5]/60}時間働いています。</p>
                <p>このペースで働きますと、月45時間以上の残業が発生する見込みです。(36協定)</p>
                <p>以下対応をお願いいたします</p>
                <ul>
                    <li>残りの業務を調整して下さい。</li>
                    <li>難しい場合は、早めに上司に相談して下さい。</li>
                </ul>
            </body>
        </html>
    """
    return html