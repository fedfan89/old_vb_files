import datetime as dt

today = dt.datetime.today()
yesterday = today + dt.timedelta(days=-1)
print(today)
print(yesterday)
