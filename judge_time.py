def judge(wt):
    if wt:
        half_wt = wt['所定時間'] / 2
        if wt['労働時間'] - half_wt >= 1500 :  # 25時間の分単位
            return True  # 残業が超過
        else:
            return False  # 残業が未超過
    else:
        return False