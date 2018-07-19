#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: foodClassArea.py 
@time: 2018/7/19 16:42 
@describe: 菜品分类
"""
from pyecharts import Pie, Page,Bar
from base.mysqlReturn import mysqlReturn


def foodClassarea(city):
    sql = '''SELECT COUNT(mainCategoryName),mainCategoryName from dazhongfood  where city="%s" GROUP BY mainCategoryName;'''%(city)
    listData = mysqlReturn(sql)
    return listData


def plotClassarea():
    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("上海")]
    [list_address.append(i[1]) for i in foodClassarea("上海")]
    print(list_address)
    print(list_sum)

    page = Page()

    pie1 = Pie("上海菜品分类", title_pos='center')
    pie1.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar1 = Bar("上海菜品分类", "数据来源于大众点评TOP100",title_pos ='center')
    bar1.add("上海", list_address, list_sum, mark_point=["max", "min"],legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("北京")]
    [list_address.append(i[1]) for i in foodClassarea("北京")]
    print(list_address)
    print(list_sum)
    pie2 = Pie("北京菜品分类", title_pos='center')
    pie2.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar2 = Bar("北京菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar2.add("北京", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("广州")]
    [list_address.append(i[1]) for i in foodClassarea("广州")]
    print(list_address)
    print(list_sum)
    pie3 = Pie("广州菜品分类", title_pos='center')
    pie3.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar3 = Bar("广州菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar3.add("广州", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("深圳")]
    [list_address.append(i[1]) for i in foodClassarea("深圳")]
    print(list_address)
    print(list_sum)
    pie4 = Pie("深圳菜品分类", title_pos='center')
    pie4.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar4 = Bar("深圳菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar4.add("深圳", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("天津")]
    [list_address.append(i[1]) for i in foodClassarea("天津")]
    print(list_address)
    print(list_sum)
    pie5 = Pie("天津菜品分类", title_pos='center')
    pie5.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar5 = Bar("天津菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar5.add("天津", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("杭州")]
    [list_address.append(i[1]) for i in foodClassarea("杭州")]
    print(list_address)
    print(list_sum)
    pie6 = Pie("杭州菜品分类", title_pos='center')
    pie6.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar6 = Bar("杭州菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar6.add("杭州", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("南京")]
    [list_address.append(i[1]) for i in foodClassarea("南京")]
    print(list_address)
    print(list_sum)
    pie7 = Pie("南京菜品分类", title_pos='center')
    pie7.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar7 = Bar("南京菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar7.add("南京", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("苏州")]
    [list_address.append(i[1]) for i in foodClassarea("苏州")]
    print(list_address)
    print(list_sum)
    pie8 = Pie("苏州菜品分类", title_pos='center')
    pie8.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar8 = Bar("苏州菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar8.add("苏州", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("成都")]
    [list_address.append(i[1]) for i in foodClassarea("成都")]
    print(list_address)
    print(list_sum)
    pie9 = Pie("成都菜品分类", title_pos='center')
    pie9.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar9 = Bar("成都菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar9.add("成都", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("武汉")]
    [list_address.append(i[1]) for i in foodClassarea("武汉")]
    print(list_address)
    print(list_sum)
    pie10 = Pie("武汉菜品分类", title_pos='center')
    pie10.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar10 = Bar("武汉菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar10.add("武汉", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("重庆")]
    [list_address.append(i[1]) for i in foodClassarea("重庆")]
    print(list_address)
    print(list_sum)
    pie11 = Pie("重庆菜品分类", title_pos='center')
    pie11.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar11 = Bar("重庆菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar11.add("重庆", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    list_address = []
    list_sum = []
    [list_sum.append(i[0]) for i in foodClassarea("西安")]
    [list_address.append(i[1]) for i in foodClassarea("西安")]
    print(list_address)
    print(list_sum)
    pie12 = Pie("西安菜品分类", title_pos='center')
    pie12.add("", list_address, list_sum, radius=[30, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical',
            legend_pos='auto', is_legend_show=False)
    bar12 = Bar("西安菜品分类", "数据来源于大众点评TOP100", title_pos='center')
    bar12.add("西安", list_address, list_sum, mark_point=["max", "min"], legend_pos="right")

    page.add(pie1)
    page.add(bar1)
    page.add(pie2)
    page.add(bar2)
    page.add(pie3)
    page.add(bar3)
    page.add(pie4)
    page.add(bar4)
    page.add(pie5)
    page.add(bar5)
    page.add(pie6)
    page.add(bar6)
    page.add(pie7)
    page.add(bar7)
    page.add(pie8)
    page.add(bar8)
    page.add(pie9)
    page.add(bar9)
    page.add(pie10)
    page.add(bar10)
    page.add(pie11)
    page.add(bar11)
    page.add(pie12)
    page.add(bar12)
    page.render("各城市菜品分类.html")
if __name__ == '__main__':
    plotClassarea()