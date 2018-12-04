import requests
from bs4 import BeautifulSoup

url = requests.get('http://politics.people.com.cn/')

url.encoding = 'GB2312'

soup = BeautifulSoup(url.text,'html.parser')

# for li in soup.select('.list_14.mt10'):
#     print(li)


url1 = 'http://politics.people.com.cn/'
url2 = 'http://politics.people.com.cn/index.html'
print(url1.find(url2))

ist1 = ['http://politics.people.com.cn/','http://politics.people.com.cn/index.html','gg']


def stringselect(aurl):
    for m in ist1:
        if m.find(url1) == 0:
            continue
        print(m)

stringselect(ist1)