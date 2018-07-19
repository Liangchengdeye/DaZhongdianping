#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: dazhongFood.py 
@time: 2018/7/18 15:46 
@describe: 大众点评美食抓取
list_city :城市的ID号码，依次是：上海，北京，广州，深圳，天津，杭州，南京，苏州，成都，武汉，重庆，西安
"""
import json
import random
import requests
from base.dbhelper import DBHelper
# 城市列表
list_city = [["上海","fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],["北京","d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],["广州","e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],["深圳","e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],["天津","2e5d0080237ff3c8f5b5d3f315c7c4a508e25c702ab1b810071e8e2c39502be1"],["杭州","91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],["南京","d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],["苏州","536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],["成都","c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],["武汉","d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],["重庆","6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],["西安","ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"]]
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]
head = {
'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}

flag = 0
code = 0
# 解析
def findFood(city,data):
    global flag,code
    mysql_db = DBHelper()
    for data in json.loads(data)["shopBeans"]:
        flag +=1
        # 详细地址
        shopAddress = data["address"]
        # 人均消费
        avgPrice = data["avgPrice"]
        # 商铺图片
        defaultPic = data["defaultPic"]
        # 分类名称
        mainCategoryName = data["mainCategoryName"]
        # 所在区域名称
        mainRegionName = data["mainRegionName"]
        # 口味评分
        tasteScore = data["score1"]
        # 环境评分
        environmentScore = data["score2"]
        # 服务评分
        serviceScore = data["score3"]
        # 商品编号
        shopId = data["shopId"]
        # 商铺网址
        shopUrl = "http://www.dianping.com/shop/"+shopId
        # 商铺名称
        shopName = data["shopName"]
        # 商铺星级
        shopPower = data["shopPower"]
        sql = '''insert into dazhongfood(shopUrl,shopName, shopId, shopPower, mainRegionName, mainCategoryName, tasteScore, environmentScore, serviceScore, avgPrice, shopAddress, defaultPic, city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (shopUrl,shopName, shopId, shopPower, mainRegionName, mainCategoryName, tasteScore, environmentScore, serviceScore, avgPrice, shopAddress, defaultPic, city)
        try:
            mysql_db.insert(sql,*params)
            code +=1
            print("----- 插入:", code, "条------")
        except:
            print("已存在不再重复插入！！")
    print("总条数：", flag)


# 抓取
def foodSpider(city_list):
    city = city_list[0]
    url = city_list[1]
    base_url = "http://www.dianping.com/mylist/ajax/shoprank?rankId="+url
    html = requests.get(base_url, headers=head)
    findFood(city=city, data=str(html.text))


if __name__ == '__main__':
    for city_data in list_city:
        foodSpider(city_data)