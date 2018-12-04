import mysql.connector

#连接数据库
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123",
    database = "newpaper"
)

#定义游标
cursor = db.cursor()

#创建表
def createtable(newpaperTable=''):
    #创表
    cursor.execute("CREATE TABLE "+newpaperTable+"(id INT NOT NULL AUTO_INCREMENT,"
                                                 "title VARCHAR(255),"
                                                 "subtitle VARCHAR(255),"
                                                 "author VARCHAR(255),"
                                                 "authorarea VARCHAR(255),"
                                                 "authordescriptions VARCHAR(255),"
                                                 "page VARCHAR(255),"
                                                 "channel VARCHAR(255),"
                                                 "abstract VARCHAR(255),"
                                                 "mainbody LONGTEXT,"
                                                 "images VARCHAR(255),"
                                                 "imagesdescriptions VARCHAR(255),"
                                                 "PRIMARY KEY(id)"
                                                 ")"
                   )


# 添加数据
def insertdata(newpaperTable='',
               title='',
               subtitle='',
               author='',
               authorarea='',
               authordescriptions='',
               page='',
               channel='',
               abstract='',
               mainbody='',
               images='',
               imagesdescriptions=''):

    sql_insert = "INSERT INTO "+newpaperTable+"(title,subtitle,author,authorarea,authordescriptions,page,channel,abstract,mainbody,images,imagesdescriptions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_values = (title,subtitle,author,authorarea,authordescriptions,page,channel,abstract,mainbody,images,imagesdescriptions)

    #添加
    cursor.execute(sql_insert,sql_values)

    #提交
    db.commit()
    print("增加成功")

#删除表
def deletetable(newpaperTable=''):
    sql_table_delete = "DROP TABLE "+newpaperTable
    cursor.execute(sql_table_delete)

# if __name__ == '__main__':
#     # createtable('sdfwe')
#     # insertdata(newpaperTable='sdfwe')
#     # deletetable('sdfwe')
