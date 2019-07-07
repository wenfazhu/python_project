#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)
mycursor = mydb.cursor()

#创建数据库
# mycursor.execute("CREATE DATABASE test_db")

#显示所有数据库
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

#在test_db创建sites表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

#给 sites 表添加主键id
#mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#设置sites表主键id自增,这一行代码的操作是前边两个的组合操作（创建表+设置主键自增id）
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

#插入单行数据到表中
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("11", "111")
# mycursor.execute(sql, val)
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")

##插入多行数据到表中
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('aaa', 'https://www.aaa.com'),
#     ('bbb', 'https://www.bbb.com'),
#     ('ccc', 'https://www.ccc.com'),
#     ('ddd', 'https://www.ddd.com/')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")

#查询sites表中的数据
# mycursor.execute("SELECT id,name,url FROM sites")
# myresult = mycursor.fetchall()     # fetchall() 获取所有记录  #fetchone()只读取一条数据
# for x in myresult:
#     print(x)

#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
# sql = "SELECT * FROM sites WHERE name = %s"
# na = ("Github", )
# mycursor.execute(sql, na)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
# sql = "select * from sites order by id desc"
# mycursor.execute(sql);
# myresult =mycursor.fetchall();
# for x in myresult:
#     print (x)

#删除记录使用 "DELETE FROM" 语句：
# sql = "DELETE FROM sites WHERE name = %s"
# # na = ("a",)
# # mycursor.execute(sql);
# # mydb.commit()
# # print(mycursor.rowcount, " 条记录删除")

#数据表更新使用 "UPDATE" 语句：
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("zwf", "zzz")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, " 条记录被修改")
