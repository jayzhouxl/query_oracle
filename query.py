#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cx_Oracle

def open_oracle():
  con=cx_Oracle.connect('yxlm_bizweb/yxlm_bizweb@198.20.1.186:1521/yxlm')
  return con

def close_oracle(con):
  con.close() 
          
def query_oracle(con,sql):
  cursor=con.cursor()

  cursor.execute(sql)
  row = cursor.fetchall() #返回的是元组列表，元组代表一行数据
  cursor.close()

  return row
