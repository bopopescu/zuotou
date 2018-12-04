
# page1 = [1,2]
# page2 = [1,2]
# list = []
# list.append(page1)
# list.append(page2)
#
# for page in list:
#     for p in page:
#         print(p)

import re

author = '编辑：李博，如有意见或建议请联系：dingjun@21jingji.com'

reg = re.compile(r'[\u4E00-\u9FA5]{2}(\：|\s)')
result = re.match(reg,author)
if result:
    print(result)
else:
    print("23")
# print(author[-1:])
# #去括号
# pattern = re.compile(r'[^\（]+(?=\）)')
# author = re.findall(pattern,author)
# author = author[len(author)-1]
# print(author)
# # author = author.encode().decode('utf-8')
# #匹配作者
# pattern = re.compile(r'[\u4E00-\u9FA5]{2}(\：|\s)[\u4E00-\u9FA5]+')
# author = re.match(pattern,author)
# author = author[0]
# print(author)
# pattern = re.compile(u'[^\s|\：]+')
# author = re.findall(pattern,author)
# author = author[len(author)-1]
# print(author)


# maxindex = len(channel)-2
# m = channel.split(channel,maxsplit=maxindex)
# print(channel[-1])
# pa = re.compile(u'[^\(]+(?=\))')
# c = re.findall(pa,channel)
# print(c[len(c)-1])
# pa = re.compile(u'[\u4e00-\u9fa5]+$')
# c = re.findall(pa,channel)
#
# for a in c:
#     print(a)