#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: foodRanging.py 
@time: 2018/7/19 10:51 
@describe:2.各大城市口味，环境，服务，及综合指数
"""
from pyecharts import Line, Bar, Page, WordCloud
import pandas as pd
from base.mysqlReturn import mysqlReturn

def foodRangingCity(city):
    sql = '''SELECT shopName,tasteScore,environmentScore,serviceScore,(tasteScore+environmentScore+serviceScore)/3.0 as avg from dazhongfood WHERE city="%s" GROUP BY (tasteScore+environmentScore+serviceScore)/3.0 DESC;'''%(city)
    listData = mysqlReturn(sql)
    listShopName = []
    listTasteScore = []
    listEnvironmentScore = []
    listServiceScore = []
    listAvg = []
    for data in listData:
        listShopName.append(data[0])
        listTasteScore.append(int(data[1]))
        listEnvironmentScore.append(int(data[2]))
        listServiceScore.append(int(data[3]))
        listAvg.append(round(data[4], 2))
    return [listShopName, listTasteScore, listEnvironmentScore, listServiceScore, listAvg]

def plotFoodRanging(list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10, list_y11, list_y12):

    page = Page()

    line1 = Line("上海饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line1.add("口味", list_y1[0], list_y1[1], mark_point=["max", "min"])
    line1.add("环境", list_y1[0], list_y1[2], mark_point=["max", "min"])
    line1.add("服务", list_y1[0], list_y1[3], mark_point=["max", "min"])
    line1.add("综合", list_y1[0], list_y1[4], mark_point=["max", "min"])
    bar1 = Bar("上海饭店评分统计", "数据来源于大众点评TOP100")
    bar1.add("上海", list_y1[0][:10], list_y1[4][:10], mark_point=["max", "min"])
    wordcloud1 = WordCloud(width=1000, height=620,background_color="#EECFA1")
    wordcloud1.add("", list_y1[0][:20], list_y1[4][:20], word_size_range=[20, 100])

    line2 = Line("北京饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line2.add("口味", list_y2[0], list_y2[1], mark_point=["max", "min"])
    line2.add("环境", list_y2[0], list_y2[2], mark_point=["max", "min"])
    line2.add("服务", list_y2[0], list_y2[3], mark_point=["max", "min"])
    line2.add("综合", list_y2[0], list_y2[4], mark_point=["max", "min"])
    bar2 = Bar("北京饭店评分统计", "数据来源于大众点评TOP100")
    bar2.add("北京", list_y2[0][:10], list_y2[4][:10], mark_point=["max", "min"])
    wordcloud2 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud2.add("", list_y2[0][:20], list_y2[4][:20], word_size_range=[20, 100])

    line3 = Line("广州饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line3.add("口味", list_y3[0], list_y3[1], mark_point=["max", "min"])
    line3.add("环境", list_y3[0], list_y3[2], mark_point=["max", "min"])
    line3.add("服务", list_y3[0], list_y3[3], mark_point=["max", "min"])
    line3.add("综合", list_y3[0], list_y3[4], mark_point=["max", "min"])
    bar3 = Bar("广州饭店评分统计", "数据来源于大众点评TOP100")
    bar3.add("广州", list_y3[0][:10], list_y3[4][:10], mark_point=["max", "min"])
    wordcloud3 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud3.add("", list_y3[0][:20], list_y3[4][:20], word_size_range=[20, 100])

    line4 = Line("深圳饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line4.add("口味", list_y4[0], list_y4[1], mark_point=["max", "min"])
    line4.add("环境", list_y4[0], list_y4[2], mark_point=["max", "min"])
    line4.add("服务", list_y4[0], list_y4[3], mark_point=["max", "min"])
    line4.add("综合", list_y4[0], list_y4[4], mark_point=["max", "min"])
    bar4 = Bar("深圳饭店评分统计", "数据来源于大众点评TOP100")
    bar4.add("深圳", list_y4[0][:10], list_y4[4][:10], mark_point=["max", "min"])
    wordcloud4 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud4.add("", list_y4[0][:20], list_y4[4][:20], word_size_range=[20, 100])

    line5 = Line("天津饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line5.add("口味", list_y5[0], list_y5[1], mark_point=["max", "min"])
    line5.add("环境", list_y5[0], list_y5[2], mark_point=["max", "min"])
    line5.add("服务", list_y5[0], list_y5[3], mark_point=["max", "min"])
    bar5 = Bar("天津饭店评分统计", "数据来源于大众点评TOP100")
    bar5.add("天津", list_y5[0][:10], list_y5[4][:10], mark_point=["max", "min"])
    wordcloud5 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud5.add("", list_y5[0][:20], list_y5[4][:20], word_size_range=[20, 100])

    line6 = Line("杭州饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line6.add("口味", list_y6[0], list_y6[1], mark_point=["max", "min"])
    line6.add("环境", list_y6[0], list_y6[2], mark_point=["max", "min"])
    line6.add("服务", list_y6[0], list_y6[3], mark_point=["max", "min"])
    line6.add("综合", list_y6[0], list_y6[4], mark_point=["max", "min"])
    bar6 = Bar("杭州饭店评分统计", "数据来源于大众点评TOP100")
    bar6.add("杭州", list_y6[0][:10], list_y6[4][:10], mark_point=["max", "min"])
    wordcloud6 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud6.add("", list_y6[0][:20], list_y6[4][:20], word_size_range=[20, 100])

    line7 = Line("南京饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line7.add("口味", list_y7[0], list_y7[1], mark_point=["max", "min"])
    line7.add("环境", list_y7[0], list_y7[2], mark_point=["max", "min"])
    line7.add("服务", list_y7[0], list_y7[3], mark_point=["max", "min"])
    line7.add("综合", list_y7[0], list_y7[4], mark_point=["max", "min"])
    bar7 = Bar("南京饭店评分统计", "数据来源于大众点评TOP100")
    bar7.add("南京", list_y7[0][:10], list_y7[4][:10], mark_point=["max", "min"])
    wordcloud7 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud7.add("", list_y7[0][:20], list_y7[4][:20], word_size_range=[20, 100])

    line8 = Line("苏州饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line8.add("口味", list_y8[0], list_y8[1], mark_point=["max", "min"])
    line8.add("环境", list_y8[0], list_y8[2], mark_point=["max", "min"])
    line8.add("服务", list_y8[0], list_y8[3], mark_point=["max", "min"])
    line8.add("综合", list_y8[0], list_y8[4], mark_point=["max", "min"])
    bar8 = Bar("苏州饭店评分统计", "数据来源于大众点评TOP100")
    bar8.add("苏州", list_y8[0][:10], list_y8[4][:10], mark_point=["max", "min"])
    wordcloud8 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud8.add("", list_y8[0][:20], list_y8[4][:20], word_size_range=[20, 100])

    line9 = Line("成都饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line9.add("口味", list_y9[0], list_y9[1], mark_point=["max", "min"])
    line9.add("环境", list_y9[0], list_y9[2], mark_point=["max", "min"])
    line9.add("服务", list_y9[0], list_y9[3], mark_point=["max", "min"])
    line9.add("综合", list_y9[0], list_y9[4], mark_point=["max", "min"])
    bar9 = Bar("成都饭店评分统计", "数据来源于大众点评TOP100")
    bar9.add("成都", list_y9[0][:10], list_y9[4][:10], mark_point=["max", "min"])
    wordcloud9 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud9.add("", list_y9[0][:20], list_y9[4][:20], word_size_range=[20, 100])

    line10 = Line("武汉饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line10.add("口味", list_y10[0], list_y10[1], mark_point=["max", "min"])
    line10.add("环境", list_y10[0], list_y10[2], mark_point=["max", "min"])
    line10.add("服务", list_y10[0], list_y10[3], mark_point=["max", "min"])
    line10.add("综合", list_y10[0], list_y10[4], mark_point=["max", "min"])
    bar10 = Bar("武汉饭店评分统计", "数据来源于大众点评TOP100")
    bar10.add("武汉", list_y10[0][:10], list_y10[4][:10], mark_point=["max", "min"])
    wordcloud10 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud10.add("", list_y10[0][:20], list_y10[4][:20], word_size_range=[20, 100])

    line11 = Line("重庆饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line11.add("口味", list_y11[0], list_y11[1], mark_point=["max", "min"])
    line11.add("环境", list_y11[0], list_y11[2], mark_point=["max", "min"])
    line11.add("服务", list_y11[0], list_y11[3], mark_point=["max", "min"])
    line11.add("综合", list_y11[0], list_y11[4], mark_point=["max", "min"])
    bar11 = Bar("重庆饭店评分统计", "数据来源于大众点评TOP100")
    bar11.add("重庆", list_y11[0][:10], list_y11[4][:10], mark_point=["max", "min"])
    wordcloud11 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud11.add("", list_y11[0][:20], list_y11[4][:20], word_size_range=[20, 100])

    line12 = Line("西安饭店评分统计", "数据来源于大众点评TOP100", width=1200)
    line12.add("口味", list_y12[0], list_y12[1], mark_point=["max", "min"])
    line12.add("环境", list_y12[0], list_y12[2], mark_point=["max", "min"])
    line12.add("服务", list_y12[0], list_y12[3], mark_point=["max", "min"])
    line12.add("综合", list_y12[0], list_y12[4], mark_point=["max", "min"])
    bar12 = Bar("西安饭店评分统计", "数据来源于大众点评TOP100")
    bar12.add("西安", list_y12[0][:10], list_y12[4][:10], mark_point=["max", "min"])
    wordcloud12 = WordCloud(width=1000, height=620, background_color="#EECFA1")
    wordcloud12.add("", list_y12[0][:20], list_y12[4][:20], word_size_range=[20, 100])

    page.add(line1)
    page.add(wordcloud1)
    page.add(bar1)

    page.add(line2)
    page.add(wordcloud2)
    page.add(bar2)

    page.add(line3)
    page.add(wordcloud3)
    page.add(bar3)

    page.add(line4)
    page.add(wordcloud4)
    page.add(bar4)

    page.add(line5)
    page.add(wordcloud5)
    page.add(bar5)

    page.add(line6)
    page.add(wordcloud6)
    page.add(bar6)

    page.add(line7)
    page.add(wordcloud7)
    page.add(bar7)

    page.add(line8)
    page.add(wordcloud8)
    page.add(bar8)

    page.add(line9)
    page.add(wordcloud9)
    page.add(bar9)

    page.add(line10)
    page.add(wordcloud10)
    page.add(bar10)

    page.add(line11)
    page.add(wordcloud11)
    page.add(bar11)

    page.add(line12)
    page.add(wordcloud12)
    page.add(bar12)

    data1 = pd.DataFrame(list_y1[4][:10], list_y1[0][:10], ["综合值"])
    print(data1)
    data2 = pd.DataFrame(list_y2[4][:10], list_y2[0][:10], ["综合值"])
    print(data2)
    data3 = pd.DataFrame(list_y3[4][:10], list_y3[0][:10], ["综合值"])
    print(data3)
    data4 = pd.DataFrame(list_y4[4][:10], list_y4[0][:10], ["综合值"])
    print(data4)
    data5 = pd.DataFrame(list_y5[4][:10], list_y5[0][:10], ["综合值"])
    print(data5)
    data6 = pd.DataFrame(list_y6[4][:10], list_y6[0][:10], ["综合值"])
    print(data6)
    data7 = pd.DataFrame(list_y7[4][:10], list_y7[0][:10], ["综合值"])
    print(data7)
    data8 = pd.DataFrame(list_y8[4][:10], list_y8[0][:10], ["综合值"])
    print(data8)
    data9 = pd.DataFrame(list_y9[4][:10], list_y9[0][:10], ["综合值"])
    print(data9)
    data10 = pd.DataFrame(list_y10[4][:10], list_y10[0][:10], ["综合值"])
    print(data10)
    data11 = pd.DataFrame(list_y11[4][:10], list_y11[0][:10], ["综合值"])
    print(data11)
    data12 = pd.DataFrame(list_y12[4][:10], list_y12[0][:10], ["综合值"])
    print(data12)
    page.render("全部.html")

if __name__ == '__main__':
    shop1 = foodRangingCity("上海")
    shop2 = foodRangingCity("北京")
    shop3 = foodRangingCity("广州")
    shop4 = foodRangingCity("深圳")
    shop5 = foodRangingCity("天津")
    shop6 = foodRangingCity("杭州")
    shop7 = foodRangingCity("南京")
    shop8 = foodRangingCity("苏州")
    shop9 = foodRangingCity("成都")
    shop10 = foodRangingCity("武汉")
    shop11 = foodRangingCity("重庆")
    shop12 = foodRangingCity("西安")
    list_x = []
    list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10, list_y11, list_y12 = [], [], [], [], [], [], [], [], [], [], [], []

    for data, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12 in zip(shop1, shop2, shop3,
                                                                                                    shop4, shop5, shop6,
                                                                                                    shop7, shop8, shop9,
                                                                                                    shop10, shop11,
                                                                                                    shop12):
        list_y1.append(data)
        list_y2.append(data2)
        list_y3.append(data3)
        list_y4.append(data4)
        list_y5.append(data5)
        list_y6.append(data6)
        list_y7.append(data7)
        list_y8.append(data8)
        list_y9.append(data9)
        list_y10.append(data10)
        list_y11.append(data11)
        list_y12.append(data12)
    plotFoodRanging(list_y1, list_y2, list_y3, list_y4, list_y5, list_y6, list_y7, list_y8, list_y9, list_y10, list_y11, list_y12)