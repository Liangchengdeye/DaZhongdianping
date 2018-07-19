#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: foodSort.py 
@time: 2018/7/18 17:57 
@describe: 商铺星级排行榜
"""
from pyecharts import Bar
from base.mysqlReturn import mysqlReturn


# 商铺评价类别
def shopCode(shopCity):
    sql = "SELECT DISTINCT(shopPower) from dazhongfood ;"
    data = mysqlReturn(sql)
    list_code = []
    for i in data:
        sql2 = '''SELECT COUNT(shopId) from dazhongfood where shopPower=%s and city="%s";'''%(i[0],shopCity)
        data_city = mysqlReturn(sql2)
        for j in data_city:
            list_code.append([i[0], j[0]])
    print(list_code)
    return list_code


# 商铺星级排行图像绘制
def plotCode(list_x, list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10, list_y11, list_y12):
    attr = list_x
    bar = Bar("各大城市饭店评分统计", "数据来源于大众点评TOP100")
    bar.add("上海", attr, list_y1, mark_point=["max","min"])
    bar.add("北京", attr, list_y2, mark_point=["max","min"])
    bar.add("广州", attr, list_y3, mark_point=["max","min"])
    bar.add("深圳", attr, list_y4, mark_point=["max","min"])
    bar.add("天津", attr, list_y5, mark_point=["max","min"])
    bar.add("杭州", attr, list_y6, mark_point=["max","min"])
    bar.add("南京", attr, list_y7, mark_point=["max","min"])
    bar.add("苏州", attr, list_y8, mark_point=["max","min"])
    bar.add("成都", attr, list_y9, mark_point=["max","min"])
    bar.add("武汉", attr, list_y10, mark_point=["max","min"])
    bar.add("重庆", attr, list_y11, mark_point=["max","min"])
    bar.add("西安", attr, list_y12, mark_point=["max","min"], is_more_utils=True, legend_top ='bottom')
    bar.render("商铺星级排名.html")


# 商铺星级排行主函数
def mianShopStar():
    shop1 = shopCode("上海")
    shop2 = shopCode("北京")
    shop3 = shopCode("广州")
    shop4 = shopCode("深圳")
    shop5 = shopCode("天津")
    shop6 = shopCode("杭州")
    shop7 = shopCode("南京")
    shop8 = shopCode("苏州")
    shop9 = shopCode("成都")
    shop10 = shopCode("武汉")
    shop11 = shopCode("重庆")
    shop12 = shopCode("西安")
    list_x = []
    list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10, list_y11, list_y12 = [], [], [], [], [], [], [], [], [], [], [], []

    for data, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12 in zip(shop1, shop2, shop3,
                                                                                                    shop4, shop5, shop6,
                                                                                                    shop7, shop8, shop9,
                                                                                                    shop10, shop11,
                                                                                                    shop12):
        if data[0] == '30':
            list_x.append("三星级")
        elif data[0] == '35':
            list_x.append("三星半")
        elif data[0] == '40':
            list_x.append("四星级")
        elif data[0] == '45':
            list_x.append("四星半")
        else:
            list_x.append("五星级")
        list_y1.append(data[1])
        list_y2.append(data2[1])
        list_y3.append(data3[1])
        list_y4.append(data4[1])
        list_y5.append(data5[1])
        list_y6.append(data6[1])
        list_y7.append(data7[1])
        list_y8.append(data8[1])
        list_y9.append(data9[1])
        list_y10.append(data10[1])
        list_y11.append(data11[1])
        list_y12.append(data12[1])
    plotCode(list_x, list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10,
             list_y11, list_y12)


if __name__ == '__main__':
    mianShopStar()