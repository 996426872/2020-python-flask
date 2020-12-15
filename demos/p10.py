import time
print(time.gmtime())
print(time.time())
print(time.localtime())
print(time.ctime())
print(time.asctime())
t = time.gmtime()
print(time.strftime("%Y-%m.%d %H:%M", t))
print(time.strptime("2020-11-30 20:36:59", "%Y-%m-%d %H:%M:%S"))
print(time.get_clock_info('perf_counter'))

import random
i = random.random()
print(i)

import re
match = re.search(r'[1-9]\d{5}', "BIT 1000081")
if match:
    print(match.group(0))
else:
    print("no match")