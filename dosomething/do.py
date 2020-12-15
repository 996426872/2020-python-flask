import json
f = open('services.json', 'r')
ll = json.loads(f.read())
print(ll, end="\n\n")
# key = servicename  value=出现次数
kk = {}
for service in ll:
    key = service['serviceName']
    val = eval(service['slowTime'])
    kk[key] = kk.get(key, 0) + val

for (key, value) in kk.items():
    print("{}:{}".format(key, value))
