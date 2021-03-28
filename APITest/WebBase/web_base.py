import requests


class WebBase:
    def __init__(self):
        self.session = requests.Session()
        self.token = self.get_token()
        self.session.params = {"access_token": self.token}

    def get_token(self):
        user_id = "ww8c3247310fc602f3"
        secret = "nj_i8kYrexQVJ4gD1xTwCVnFrOr8t9HW5WnSBavC84w"
        token = self.session.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={user_id}&corpsecret={secret}")
        return token.json()["access_token"]

    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)
