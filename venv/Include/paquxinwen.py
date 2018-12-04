from urllib import request
from bs4 import BeautifulSoup

url = "https://www.163.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

page = request.Request(url,headers=headers)
page_info = request.urlopen(page).read().decode('gbk')

soup = BeautifulSoup(page_info,'html.parser')

titles = soup.find_all('a','title');

# for links in title:
#     print(links.get('href'))

with open(r"D:\软件\update\python\title.txt","w") as file:
    for title in titles:
        # file.write(title.string +'\n')
        file.write(title.get('href')+'\n\n')