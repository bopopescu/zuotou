import os

# 文章字典
artpage = {'title': '',
           'subtitle': '',
           'author': '',
           'authorarea': '',
           'authordescriptions': '',
           'page': '',
           'channel': '',
           'abstract': '',
           'mainbody': '',
           'images': '',
           'imagesdescriptions': ''}

# 文章内容
titlelist = ''
subtitlelist = ''
authorlist = ''
authorarealist = ''
authordescriptionslist = ''
pagelist = ''
channellist = ''
abstractlist = ''
mainbodylist = ''
imageslist = ''
imagesdescriptionslist = ''

#保存新闻
newpeaper = []

def getfilename():
    filename = os.path.basename(os.path.realpath(__file__))
    print(filename)


# if __name__ == '__main__':
#     getfilename()