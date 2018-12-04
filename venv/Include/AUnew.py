from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as Ex
import time

#打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(10)
actions = ActionChains(driver)
driver.get("http://globe2go.newspaperdirect.com/epaper/viewer.aspx")
driver.maximize_window();

# 登陆
driver.find_element_by_id("signin").click()
driver.find_element_by_id("_ctl0__ctl0_MainContentPlaceHolder_MainPanel__ctl4_login__ctl0_UserName").send_keys("13574827001@163.com")
driver.find_element_by_id("_ctl0__ctl0_MainContentPlaceHolder_MainPanel__ctl4_login__ctl0_Password").send_keys("Yyy13579")
driver.find_element_by_id("login_existing_user_login_btn").click()

driver.switch_to.frame("content_frame")
time.sleep(1)
driver.find_element_by_xpath("//DIV[@class='se-t2-supp_float']/DIV[1]").click()

driver.switch_to.default_content()
actions.move_to_element(driver.find_element_by_xpath("//SPAN[@id='toc']"))
actions.click()
actions.perform()
time.sleep(2)

actions.move_to_element(driver.find_element_by_id("toc_1")).perform()
time.sleep(1)
driver.find_element_by_xpath("//DIV[@id='toc_submenu_menubody']/DIV[2]").click()

actions.release()

# 文章
driver.switch_to.frame("content_frame")
driver.switch_to.frame("content_window_frame_elm")

nextpage = driver.find_elements_by_xpath("//DIV[@class='art-storyorder']/A[@class='button-big button-big-forward']")
while nextpage != None:
    try:
        title = driver.find_element_by_xpath("//DIV[@class='art-content']//H1")
        author = driver.find_elements_by_xpath("//UL[@class='art-meta']/LI")
        mainbody = driver.find_elements_by_xpath("//DIV[@class='clear']//P")
        images = driver.find_elements_by_xpath("//DIV[@class='clear']//IMG|//IMG[@id='magnified_image']|//IMG[@id='artObject']")
        imagesdes = driver.find_elements_by_xpath("//DIV[@id='testArtCol_a']//SPAN[@class='art-imagetext']")

        driver.switch_to.default_content()
        driver.switch_to.frame("content_frame")

        channel = driver.find_element_by_xpath("//SPAN[@id='content_window_title']")
        page = driver.find_element_by_xpath("//SPAN[@id='content_window_title']")

        driver.switch_to.frame("content_window_frame_elm")
        # 打印
        print(title.text)
        for a in author:
            print(a.text+"\n")
        for m in mainbody:
            print(m.text+"\n")
        for i in images:
            print(i.get_attribute("src")+"\n")
        for id in imagesdes:
            print(id.text+"\n")
        # print(page.text)
        # print(channel.text)
        # 下一篇
        flag = True
        while flag:
            try:
                nextpage[1].click()
                flag = False
            except Ex.StaleElementReferenceException:
                print()
    except Ex.NoSuchElementException:
        print()
    except Ex.ElementNotVisibleException:
        break

print("结束")