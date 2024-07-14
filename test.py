import datetime


tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
today = datetime.datetime.now(tokyo_tz).day

print(today === 15)