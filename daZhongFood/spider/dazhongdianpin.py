#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: dazhongdianpin.py 
@time: 2018/8/1 10:32 
@describe: 抓取大众点评评论信息
"""
import csv
import requests
from pyquery import PyQuery as pq

headers = {
    'Host': 'www.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
    'Accept-Encoding': 'gzip',
}


def spiderDazhong(ID):
    try:
        html = requests.get("http://www.dianping.com/shop/%s/review_all"%(ID), headers=headers)
        doc = pq(html.text)
        if doc:
            # 存入csv文件
            out = open('./data/Stu_csv.csv', 'a', newline='',encoding="utf-8")
            # 设定写入模式
            csv_write = csv.writer(out, dialect='excel')
            shopName = doc("div.review-list-header > h1 > a").text()
            shopurl = "http://www.dianping.com"+doc("div.review-list-header > h1 > a").attr("href")
            csv_write.writerow(["店铺名称","店铺网址"])
            csv_write.writerow([shopName,shopurl])
            csv_write.writerow(["用户名", "用户ID链接", "评定星级", "评论描述", "评论详情", "评论时间", "评论商铺", "评论图片"])
            # 解析评论
            pinglunLi = doc("div.reviews-items > ul > li").items()
            for data in pinglunLi:
                userName = data("div.main-review > div.dper-info > a").text()
                userID = "http://www.dianping.com"+data("div.main-review > div.dper-info > a").attr("href")
                startShop = str(data("div.review-rank > span").attr("class")).split(" ")[1].replace("sml-str","")
                describeShop = data("div.review-rank > span.score").text()
                pinglunShop = data("div > div.review-words").text().replace("收起评论","").replace(" ","").replace("\n","")
                timeShop = data("div.main-review > div.misc-info.clearfix > span.time").text()
                Shop = data("div.main-review > div.misc-info.clearfix > span.shop").text()
                imgShop = data("div > div.review-pictures > ul > li> a").items()
                imgList = []
                for img in imgShop:
                    imgList.append("http://www.dianping.com"+img.attr("href"))

                # 写入具体内容
                csv_write.writerow([userName,userID,startShop,describeShop,pinglunShop,timeShop,Shop,imgList])
                print("successful insert csv!")

    except Exception as e:
        print("error",str(e))


if __name__ == '__main__':
    # 代表各大商铺ID，可通过商铺列表页回去
    listShop = ["2972056", "91018291","69952338"]
    for shop in listShop:
        spiderDazhong(shop)