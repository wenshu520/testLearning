import json

from mitmproxy import http

class AD:
    def request(self, flow):
        pass

    def response(self, flow:http.HTTPResponse):
        # print("url8888888" + flow.request.pretty_url)
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?" in flow.request.pretty_url:
            res = json.loads(flow.response.text)
            res["data"]["items"][0]["market"]["status"] = "WenshuTesting"
            flow.response.text = json.dumps(res)

addons = [
    AD()
]