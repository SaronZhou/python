# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:13:36 2019

@author: admin
"""

import sqlite3

# 创建SQLite3内存数据库
# 创建带有4个属性的sales表
# 创建连接对象con，':memory:'是一个专用名称
# 使用字符串 'My_database.db' 或 'C:\Users\Clinton\Desktop\my_database.db'可以持久化数据库
con = sqlite3.connect(':memory:')
query = '''CREATE TABLE sales 
            (customer VARCHAR(20),
             produce VARCHAR(20),
             amount FLOAT,
             date DATE);'''
# 使用连接对象的execute方法执行query中的SQL命令
con.execute(query)
# 使用连接对象的commit方法保存修改到数据库
con.commit()

# 在表中插入几行数据
data =  [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
         ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
         ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
         ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
# ？在此处用作占位符，表示想在SQL命令中使用的值
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
# executemany方法为data中每个数据元组执行变量statement中的SQL命令
con.executemany(statement, data)
con.commit()

# 查询sales表
cursor = con.execute("SELECT * FROM sales")
# 使用fetchall方法取出结果集中所有行
rows = cursor.fetchall()

# 计算查询结果中行的数量
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: %d' % row_counter)


# 向表中插入新纪录 #
import csv
import sqlite3

input_file = "supplier_data.csv"
con = sqlite3.connect('Suppliers.db')
# 创建一个游标对象
c = con.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);'''
c.execute(create_table)
con.commit()

# 读取csv文件
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()

# 查询Suppliers表
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)
    
    
# 更新表中记录
import csv
import sqlite3  
  
input_file = "data_for_updating.csv"
con = sqlite3.connect(':memory:')
query = '''CREATE TABLE sales 
            (customer VARCHAR(20),
             produce VARCHAR(20),
             amount FLOAT,
             date DATE);'''
con.execute(query)
con.commit()

# 向表中插入几行数据
data =  [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
         ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
         ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
         ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# 读取csv文件并更新特定的行
file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)
con.commit()

# 查询sales表
cursor = con.execute("SELECT *FROM sales")
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)
    
    
    
    