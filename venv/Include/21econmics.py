from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Ex
import time
from Include import mysqldb
import re
from Include import entity

def ecomicsepaper():
    # 站点的电子报路径    21世纪经济报道
    url = 'http://epaper.21jingji.com/'

    # 声明驱动
    driver = webdriver.Chrome()

    # 声明等待
    wait = WebDriverWait(driver, 10)

    # 鼠标行动
    actions = ActionChains(driver)

    # 访问站点
    driver.get(url)

    # 窗口最大化
    driver.maximize_window()

    # 文章获取目录
    artpage = driver.find_elements_by_xpath("//DIV[@class='news_list']/UL/LI/A/SPAN")

    # 文章遍历
    for p in artpage:
        # 选择文章
        p.click();
        cont = p.text
        #进入文章窗口
        winmub = driver.window_handles
        driver.switch_to.window(winmub[1])

        if cont != '广告':
            #获取内容
            try:
                title = driver.find_element_by_xpath("//DIV[@class='news_content']/H1[2]")
            except Ex.NoSuchElementException:
                print()
            try:
                author = driver.find_element_by_xpath("//DIV[@class='news_text']/p[last()]")
            except Ex.NoSuchElementException:
                print()
            try:
                mainbody = driver.find_elements_by_xpath("//DIV[@id='news_text']/P")
            except Ex.NoSuchElementException:
                print()
            try:
                images = driver.find_elements_by_xpath("//DIV[@class='news_photo']/TABLE/TBODY/TR/TD/IMG")
            except Ex.NoSuchElementException:
                print()
            #打印
            print(title.text + "\n")

            # print(author.text + "\n")
            #作者
            author = author.text
            lastauthor = author[-1:]
            if lastauthor == ')':
                #英文括号
                #去括号
                pattern = re.compile(u'[^\(]+(?=\))')
                m = re.findall(pattern,author)
                author = m[len(m)-1]
                #匹配作者
                pattern = re.compile(u'^[\u4e00-\u9fa5]{2}(\：|\s)[\u4e00-\u9fa5]+')
                author = re.match(pattern,author)
                author = author[0]
                pattern = re.compile(u'[^\s|\：]+')
                author = re.findall(pattern,author)
                author = author[len(author)-1]
                print(author)
            elif lastauthor == '）':
                #去括号
                pattern = re.compile(u'[^\（]+(?=\）)')
                author = re.findall(pattern,author)
                author = author[len(author)-1]
                #匹配作者
                reg = re.compile('[\u4E00-\u9FA5]{2}(\：|\s)')
                result = re.match(reg,author)
                if result:
                    pattern = re.compile(u'[\u4e00-\u9fa5]{2}(\：|\s)[\u4e00-\u9fa5]+')
                    author = re.match(pattern, author)
                    author = author[0]
                    pattern = re.compile(u'[^\s|\：]+')
                    author = re.findall(pattern, author)
                    author = author[len(author) - 1]
                    print(author)
                else:
                    print(author)
            else:
                print(author)

            for mb in mainbody:
                print("<p>" + mb.text + "</p>" + "\n")
            for im in images:
                print(im.get_attribute('src') + "\n")

            print("*--------------------------------------------*")

        #关闭文章窗口
        driver.close()
        driver.switch_to.window(winmub[0])

    print("结束")




if __name__ == '__main__':
    ecomicsepaper()

