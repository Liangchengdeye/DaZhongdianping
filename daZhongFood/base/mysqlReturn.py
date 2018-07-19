#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: mysqlReturn.py 
@time: 2018/7/19 10:52 
@describe: 基础组件-mysql结果集返回
"""
# mysql结果返回
from base.dbhelper import DBHelper


def mysqlReturn(sql):
    mysql_db = DBHelper()
    return mysql_db.select(sql)