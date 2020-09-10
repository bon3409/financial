import os
import requests
from dotenv import load_dotenv # 讀取 env 檔

# 參考資料: https://bustlec.github.io/note/2018/07/10/line-notify-using-python/
# 紀錄 Line Notify 的實用功能，並模組化

class LineNotify():
    def lineNotifyMessage(msg: str):
        ''' 傳送訊息到 Line Notify '''

        # 取得 env 的資訊
        load_dotenv()
        token = os.getenv('LINE_NOTIFY_TOKEN')

        headers = {
            "Authorization": "Bearer " + token, 
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
