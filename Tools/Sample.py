from LineService import service

# 訊息內容
message = '通知測試'

# 使用模組的 function，透過 line notify 傳送訊息
line = service()

line.lineNotifyMessage(message)
