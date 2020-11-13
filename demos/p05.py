import requests

h = {
    "Host": "www.kuaidi.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3620.400",
    "Referer": "http://www.kuaidi.com/",
}

url = '''http://www.kuaidi.com/index-ajaxselectcourierinfo-552027047111994-huitongkuaidi-XCAO1605165158370.html'''


r = requests.post(url, headers=h)
print(r.json())
result = r.json()
data = result['data']
print("快递单号：{}".format(result['nu']))
print("company：{}".format(result['company']))
print("最新状态：{}".format(data[0]['context']))
