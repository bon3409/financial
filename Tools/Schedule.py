import time
import schedule
import datetime
from LineService import service

# 利用 schedule 傳送訊息到 line
  
def job():
    message = 'schedule 的測試(每五秒)'
    print(datetime.datetime.now())
    line = service()
    line.lineNotifyMessage(message)

# schedule 的執行間隔
schedule.every(5).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
  
while True:
    schedule.run_pending()
    time.sleep(1)