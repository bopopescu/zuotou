from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import xdrlib,sys
import xlrd
import xlwt

# 打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://fanyi.youdao.com/")


# 翻译
def chramefy(nr = '',list=[]):
    driver.find_element_by_id("inputOriginal").send_keys(nr)
    time.sleep(10)
    driver.find_element_by_id("langSelect").click()
    loacator = (By.ID,"transTarget")
    try:
        WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(loacator))
    finally:
        print("*-----------------------------------------------------*")
    content = driver.find_element_by_id("transTarget")
    print(content.text)
    list.append(content.text)
    driver.find_element_by_id("inputOriginal").clear()


# 导入excel
def open_excel(file='beijing.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception(e):
        print(str(e))

idv=[]
def excel_table_byname(file = 'beijing.xls',colnameindex=0,by_name=u'sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    list=[]
    for rownum in range(0,nrows):
        row = table.row_values(rownum)
        if row:
            if row[5]:
                chramefy(row[5],list)
                idv.append(row[0])
    return list

list = excel_table_byname()
print(len(list))
print(len(idv))
# 保存到新的excel
workbook = xlwt.Workbook(encoding='UTF-8')
booksheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
for i in range(len(list)):
    booksheet.write(i,0,idv[i])
    booksheet.write(i,1,list[i])

workbook.save("D:/work/图片/china.xls")

