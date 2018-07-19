#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: W_H_J
@license: Apache Licence
@contact: 415900617@qq.com
@site:
@software: PyCharm
@file: dbhelper.py
@time: 2018/1/17 17:46
@describe: 数据库操作助手

"""
import pymysql


# 此类操作数据库
class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'
        self.db = 'dazhongdianping'

    # 连接到mysql，不是连接到具体的数据库
    def connectMysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               # db=self.db,不指定数据库名
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

    # 连接到具体的数据库（settings中设置的MYSQL_DBNAME）
    def connectDatabase(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

        # 创建数据库

    def createDatabase(self):
        '''因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不要传sql语句了'''
        conn = self.connectMysql()  # 连接数据库

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)  # 执行sql语句
        cur.close()
        conn.close()

    # 创建表
    def createTable(self, sql):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    # 插入数据
    def insert(self, sql, *params):  # 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    # 更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    # 删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    # 查询数据
    def select(self, sql):
        conn = self.connectDatabase()
        cur = conn.cursor()
        try:
            # 执行SQL语句
            cur.execute(sql)
            conn.commit()
            # 获取所有记录列表
            results = cur.fetchall()
            return results
        except:
            print("Error: unable to fecth data")
        cur.close()
        conn.close()


'''测试DBHelper的类'''


class TestDBHelper():
    def __init__(self):
        self.dbHelper = DBHelper()

    # 测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDatebase(self):
        self.dbHelper.createDatabase()
        # 测试创建表

    def testCreateTable(self):
        sql = "create table testtable(id int primary key auto_increment,name varchar(50),url varchar(200))"
        self.dbHelper.createTable(sql)

    # 测试插入
    def testInsert(self, item):
        sql = "insert into testtable(name,url) values(%s,%s)"
        # params=("Ncepu_Etl","Ncepu_Etl")
        params = (item["name"], item["url"])
        self.dbHelper.insert(sql, *params)  # *表示拆分元组，调用insert（*params）会重组成元组

    def testUpdate(self):
        sql = "update testtable set name=%s,url=%s where id=%s"
        params = ("update", "update", "1")
        self.dbHelper.update(sql, *params)

    def testDelete(self):
        sql = "delete from testtable where id=%s"
        params = ("1")
        self.dbHelper.delete(sql, *params)

    def testSelect(self):
        sql = "select * from testtable"
        # params=("1")
        self.dbHelper.select(sql)


if __name__ == "__main__":
    pass
    testDBHelper = TestDBHelper()
    # testDBHelper.testCreateDatebase()  #执行测试创建数据库
    # testDBHelper.testCreateTable()     #执行测试创建表
    # testDBHelper.testInsert()          #执行测试插入数据
    # testDBHelper.testUpdate()          #执行测试更新数据
    # testDBHelper.testDelete()          #执行测试删除数据
    # testDBHelper.testSelect()          #执行测试查询数据