import urllib.request
from PIL import Image

def dowpothon():

    f = open("D:\\work\\图片\\12.jpg",'wb')
    f.write((urllib.request.urlopen("http://buy.yicai.com/p/verify.html??????")).read())


if __name__ == '__main__':
    dowpothon()