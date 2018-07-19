#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: foodSynthesize.py 
@time: 2018/7/19 16:52 
@describe: 综合评价
"""
from pyecharts import Radar, Page

from base.mysqlReturn import mysqlReturn


def foodRangingCity(city,shopName):
    sql = '''SELECT shopName,tasteScore,environmentScore,serviceScore,avgPrice,shopPower from dazhongfood WHERE city="%s" and shopName="%s";'''%(city,shopName)
    listData = mysqlReturn(sql)
    return listData

def plotSynthesize():
    schema = [
        ("口味", 100), ("环境", 100), ("服务", 100),
        ("人均", 250), ("星级", 50)
    ]
    list_shopName = ['天素无界蔬食餐厅', '梵', '肉魁屋烧肉酒场', '锋哥的馆子', '淮扬府·游园京梦', '随遇·青涩小馆·之·未央28楼','串一火锅', '美阳馆', '张老板的店', '板•菋']
    page = Page()
    for i in range(len(list_shopName)):
        list_select = foodRangingCity("西安", list_shopName[i])
        print(list_shopName[i], list(list_select[0])[1:])
        v2 = [list(list_select[0])[1:]]
        radar = Radar()
        radar.config(schema)
        radar.add(list_select[0][0], v2, label_color=["red"], is_area_show=False,
                  legend_selectedmode='single')
        page.add(radar)
    page.render("综合评价.html")


if __name__ == '__main__':
    plotSynthesize()