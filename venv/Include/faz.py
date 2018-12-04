from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Ex
import time
from Include import mysqldb

# 法兰克福汇报
def faznewpaper():
    #站点的电子报路径    法兰克福汇报
    url = 'http://www.faz.net/aktuell/'

    #声明驱动
    driver = webdriver.Chrome()

    # 声明等待
    wait = WebDriverWait(driver,10)

    #鼠标行动
    actions = ActionChains(driver)

    #访问站点
    driver.get(url)

    #窗口最大化
    driver.maximize_window()

    #登陆
    wait.until(EC.element_to_be_clickable((By.XPATH,"//HEADER[@role='banner']//UL[@class='gh-MainNav_Aux']/LI[@class='gh-MainNav_AuxItem']/A[@class='js-lay-Login_Open gh-MainNav_AuxLink gh-MainNav_AuxLink-is-last']")))
    driver.find_element_by_xpath("//HEADER[@role='banner']//UL[@class='gh-MainNav_Aux']/LI[@class='gh-MainNav_AuxItem']/A[@class='js-lay-Login_Open gh-MainNav_AuxLink gh-MainNav_AuxLink-is-last']").click()

    wait.until(EC.presence_of_element_located((By.ID,"iframe-loginbox-form")))
    driver.switch_to.frame('iframe-loginbox-form')

    driver.find_element_by_xpath("//DIV[@class='o-Grid']//INPUT[@name='loginName']").send_keys("lizhuoqun")
    driver.find_element_by_xpath("//DIV[@class='o-Grid']//INPUT[@name='password']").send_keys("Yyy123456")
    driver.find_element_by_xpath("//A[@class='btn-Base_Link']/SPAN[@class='btn-Base_Text']").click()

    #进入电子报
    wait.until(EC.element_to_be_clickable((By.XPATH,"//UL[@class='gh-Cta']/LI[2]/A/SPAN")))
    driver.find_element_by_xpath("//UL[@class='gh-Cta']/LI[2]/A/SPAN").click()

    driver.find_element_by_xpath("//DIV[@class='row newspapers-row']/DIV[1]//DIV[@class='newspaper-cover-inner']/A").click()

    wait.until(EC.element_to_be_clickable((By.XPATH,"//A[@class='paginator-element nextPage']")))
    nextbtn = driver.find_element_by_xpath("//A[@class='paginator-element nextPage']")

    #报纸的文章
    newpage = []

    while(nextbtn != None):
        time.sleep(3)
        #文章列表
        artpage = driver.find_elements_by_xpath("//DIV[@class='availableBox ng-scope']/DIV[@class='avBoxContainer ng-scope']/DIV")

        #获取文章
        for ap in artpage:
            #内容集合
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

            try:
                #进入文章
                ap.click()

                #采集文章内容
                title = driver.find_element_by_id("avHauptzeile")
                subtitle = driver.find_elements_by_id("avUnterzeile")
                channel = driver.find_element_by_id("avIssueTitle")
                abstracts = driver.find_elements_by_xpath("//*[@id='avTeaser']")
                mainbody = driver.find_elements_by_xpath("//*[@id='avText']/p")
            except Exception:
                print()
            #打印
            # print(title.text+'\n')
            # for st in subtitle:
            #     sub1.append("<p>"+st.text+"</p>")
            #     print(st.text + '\n')
            # print(channel.text+'\n')
            # for ab in abstracts:
            #     abs1.append("<p>"+ab.text+"</p>")
            #     print(ab.text + '\n')
            # for mb in mainbody:
            #     mbd1.append("<p>"+mb.text+"</p>")
            #     print(mb.text + '\n')
            #
            # print("*----------------------------------------------------------*")

            #内容保存到集合
            titlelist = titlelist + (title.text)
            for st in subtitle:
                subtitlelist = subtitlelist + ("<p>"+st.text+"</p>")
            for ab in abstracts:
                abstractlist = abstractlist + ("<p>"+ab.text+"</p>")
            for mb in mainbody:
                mainbodylist = mainbodylist + ("<p>"+mb.text+"</p>")

                # 文章字典
                artpage = {'title': titlelist,
                           'subtitle': subtitlelist,
                           'author': authorlist,
                           'authorarea': authorarealist,
                           'authordescriptions': authordescriptionslist,
                           'page': pagelist,
                           'channel': channellist,
                           'abstract': abstractlist,
                           'mainbody': mainbodylist,
                           'images': imageslist,
                           'imagesdescriptions': imagesdescriptionslist}

            try:
                #关闭文章框
                driver.find_element_by_xpath("//DIV[@class='close']").click()
            except Exception:
                print()

            newpage.append(artpage)
        try:
            nextbtn.click()
        except Ex.ElementNotVisibleException:
            break
    return newpage
    print("结束")


#加到数据库
def addNewparper():
    #创表
    mysqldb.createtable('Faznewpaper')
    try:
        #加数据
        newpage = faznewpaper()
        for p in newpage:
            mysqldb.insertdata('Faznewpaper',
                               title=p['title'],
                               subtitle=p['subtitle'],
                               author=p['author'],
                               authorarea=p['authorarea'],
                               authordescriptions=p['authordescriptions'],
                               page=p['page'],
                               channel=p['channel'],
                               abstract=p['abstract'],
                               mainbody=p['mainbody'],
                               images=p['images'],
                               imagesdescriptions=p['imagesdescriptions']
                               )
    except Exception as e:
        # mysqldb.deletetable('Faznewpaper')
        print(e)
        print("添加失败")
def main():
    addNewparper()

if __name__ == '__main__':
    main();