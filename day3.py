# requests


import requests
import json

'''
phone = "18319022476"
key = "21433fc3b710f52c5c18cb5e44b284db"
link = "https://apis.juhe.cn/mobile/get"
par = {
    "phone": phone,
    "key": key
}
r = requests.get(url=link, params=par)
t = r.content.decode()
print(t)
# l = json.loads(t)
# print(l, type(l))
'''

link1 = "http://apis.juhe.cn/simpleWeather/query"
par1 = {
    "key": "ff9fd397372af8459a850709f10fed93",
    "city": 1
}

r1 = requests.post(url=link1, data=par1)
#print(r1.headers['Date'], r1.headers['Content-Type'])
print(r1.status_code)
print(r1.content.decode())
print(r1.headers)
print(dict(r1.headers))



r2 = requests.post()


