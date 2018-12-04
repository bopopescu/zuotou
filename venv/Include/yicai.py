from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Ex
import time
from Include import mysqldb
import re


def yicaipaper():
    # 站点的电子报路径    21世纪经济报道
    url = 'http://buy.yicai.com/read/index/id/5.html'

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

    # #报纸
    # driver.find_element_by_xpath("//DIV[@class='left_menu']/DIV[6]//A").click()
    #
    # #选择窗口
    # win = driver.window_handles
    # # driver.close()
    # driver.switch_to.window(win[1])

    #登陆
    cookie = {"domain":"buy.yicai.com",
              'name':'PHPSESSID',
              'value':'a890df996d5f623b1cc8d04148212848',
              'path':'/',
              'httpOnly':False,
              'HostOnly':False,
              'Secure':False
    }
    driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()

    # time.sleep(100000)
    nextpage = driver.find_element_by_xpath("//DIV[@id='ShowConMain']//DIV[@class='navbar-inner']/DIV[2]/LI[2]/A")

    while nextpage != None:
        #获取内容
        title = driver.find_element_by_xpath("//DIV[@class='conrand']//FONT[@class='SetTitle']")
        subtitle = driver.find_elements_by_xpath("//*[@id='SetsubTitle']")
        author = driver.find_element_by_xpath("//SPAN[@id='Setauthor']")
        page = driver.find_element_by_xpath("//FONT[@id='SetNumber']")
        channel = driver.find_element_by_xpath("//STRONG[@class='picBName']//A")
        mainbody = driver.find_elements_by_xpath("//*[@id='SetContent']/P")
        images = driver.find_elements_by_xpath("//*[@id='SetContent']/div/div[1]/img")
        imagesdescription = driver.find_elements_by_xpath("//*[@id='SetContent']/div/div[last()]")

        #打印
        print(title.text + "\n")
        for st in subtitle:
            print(st.text + "\n")
        print(author.text)
        try:
            print(page.text + "\n")
        except Ex.StaleElementReferenceException as e:
            print()
        try:
            channel = channel.text
            if channel:
                pattern = re.compile(u'[\u4e00-\u9fa5]+$')
                rechannel = re.findall(pattern, channel)
                for channel in rechannel:
                    print(channel + "\n")
        except Ex.StaleElementReferenceException as e:
            print()
        try:
            for mb in mainbody:
                print("<p>" + mb.text + "</p>" + "\n")
        except Ex.StaleElementReferenceException as e:
            print()
        for im in images:
            print( im.get_attribute('src') + "\n")
        try:
            for imd in imagesdescription:
                print(mb.text + "\n")
        except Ex.StaleElementReferenceException as e:
            print()
        #下一篇
        nextpage.click()

        try:
            alert = driver.switch_to.alert;
            break
        except Ex.NoAlertPresentException:
            pass


if __name__ == '__main__':
    yicaipaper()