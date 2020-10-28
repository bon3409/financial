import ffn
from datetime import date

class stock():
    def __init__(self):
        super().__init__()

    def getData(self, code, start_day):
        return ffn.get(f"{code}:Open, {code}:High, {code}:Low, {code}:Close", start=start_day)