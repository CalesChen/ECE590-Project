import urllib.request
import time
import random
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
url = "https://xcxvr.icbc.com.cn/newService/mmsp/index.html?userId=160300441#/"
i = 0
while(i < 50):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    #time.sleep(random.randint(10,30))
    i += 1

print(data)