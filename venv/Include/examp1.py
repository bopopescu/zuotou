import urllib.request
from _socket import timeout
from datetime import time
import  urllib.parse

url = 'http://www.qstheory.cn/dukan/qs/2017-12/31/c_1122175484.htm'
response = urllib.request.urlopen(url,timeout=1) #timeout设置超时
html = response.read()
# print(html.decode('utf-8'))

params = {
    'name' : 'zzy',
    'paw' : '123'
}
# data = bytes(urllib.parse.urlencode(params),encoding='utf-8')
# response = urllib.request.urlopen(url,data=data)
# print(response.read().decode('utf-8'))
#urlopen发起简单请求

#Request
# url = 'https://app.nytimes.com/'
url = 'http://www.qikan.com.cn/articleinfo/lwdf20184005.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

#代理
proxy_handler = urllib.request.ProxyHandler({
    'https':'119.187.74.220:20537',
    # 'http':'118.190.95.35:9001',
    #  'https':'203.86.26.9:3128'
     'https':'61.128.208.94:3128'
})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))