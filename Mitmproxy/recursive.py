import json

from mitmproxy import http

def handle_data(data):
    if isinstance(data, list):
        for ele in data:
            handle_data(ele)
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = handle_data(value)
    elif isinstance(data, str):
        data = data + "AA"
    elif isinstance(data, (int, float)):
        data = data * 2
    else:
        data = data
    return data

class AD():
    def request(self, flow):
        pass
    def response(self, flow: http.HTTPResponse):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?" in flow.request.pretty_url:
            res = json.loads(flow.response.text)
            modified_data = handle_data(res)
            print(modified_data)
            flow.response.text = json.dumps(modified_data)


addons = [
    AD()
]
