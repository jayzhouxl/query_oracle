#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv

def read_col_from_csv(csv_file_name,col_num):
  csv_data = csv.reader(open(csv_file_name,'r'))

  col_data = []
  #每一行都是list
  for row in csv_data:
    col_data.append(row[col_num-1].strip())

  sql_sep = "','"
  sql_par_1 = sql_sep.join(col_data)
  sql_par_1 = "'" + sql_par_1 + "'"

  return sql_par_1

def joint_sql(sql_par):
   sql_par_1 =''
   sql_par_2 = ''
   sql = sql_par_1 + sql_par + sql_par_2
  return sql


if __name__ == "__main__":
  sql_par=read_col_from_csv("1.csv",1)
  sql = joint_sql(sql_par)
  print sql
