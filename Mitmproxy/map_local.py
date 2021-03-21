from mitmproxy import http

class AD():
    def request(self, flow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?" in flow.request.pretty_url:
            with open("Mitmproxy/xueqiu.json", encoding="utf-8") as xueqiu:
                flow.response = http.HTTPResponse.make(200,
                                                       xueqiu.read(),
                                                       {"Content-Type": "text/html"})

    def response(self, flow):
        pass

addons = [
    AD()
]