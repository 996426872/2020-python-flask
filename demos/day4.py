import requests


r1 = requests.get("https://wwww.baidu.com")
print(r1.headers)
cok = r1.headers['Set-Cookie']
# print(type(cok))

cokes = r1.cookies

r2 = requests.get(url="https://wwww.baidu.com")
# r2 = requests.get(url="https://wwww.baidu.com", cookies=cokes)
print(r2.headers)
# print(r2.content)
