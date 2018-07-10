#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import op_file #这种import以后函数调用必须op_file.xxx()
#import query
import os
import sys
import csv
import codecs
from op_file import *
from query import *

#reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入 
#sys.setdefaultencoding('utf-8')

def op_val(key,query_val,query_val_temp):
  val = ''
  sep = ','
  val_list = []

  for val in query_val:
    val_list.append(key + '\t,' + '\t,'.join(str(s) for s in list(val)) + '\t,' + '\t,'.join(str(s) for s in query_val_temp[0]) + '\r')

  return val_list

def write_org_file(file_name,val_list):
  title = '标题\r' #windows换行符\r\n 
  title_gb = title.decode('utf-8').encode('GB2312')
  file_name = './org/' + file_name
  result_file = open(file_name,'ab')
  if result_file.tell() == 0:
    result_file.write(title_gb)
  result_file.writelines(val_list)

  result_file.close()

if __name__ == "__main__":
  sql_file = open_file("sql.txt",'rU') #U通用换行模式（Universal new line mode）。该模式会把所有的换行符（\r \n \r\n）替换为\n

  #res_file = codecs.open("res.csv","wb",encoding='GBK')

  lines = read_file(sql_file)
  close_file(sql_file)

  db_obj = open_oracle()

  line_count = 0

  for line in lines:
    line_count += 1
    line_lis = line.split('\x03')
    org_code = line_lis[0]
    res_name = org_code + '.csv'
    key = line_lis[1]
    sql = line_lis[2]
    temp_sql = "select shop_name,address from tbl_ope_biz_shop where shop_no = '" + key + "'"
    query_val_temp = query_oracle(db_obj,temp_sql)

    query_val = query_oracle(db_obj,sql)
    res_list = op_val(key,query_val,query_val_temp)
    write_org_file(res_name,res_list)

  close_oracle(db_obj)
