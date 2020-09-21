import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = "yassine", passwd = "root",database = "newdb")

my_cursor = db.cursor()

"""CREATE A DATABASE"""
q_cre_db = "CREATE DATABASE newdb"
my_cursor.execute(q_cre_db)

"""CREATE A Table"""
q_cre_table = "CREATE TABLE customers(name varchar(50), address varchar(100), id int PRIMARY KEY auto_increment)"
my_cursor.execute(q_cre_table)

"""SHOW TABLES"""
q_show = "SHOW tables"
my_cursor.execute(q_show)
for x in my_cursor:
	print(x)


"""Add a column to an existing table"""
q_alter = "ALTER table customers add column id int PRIMARY KEY auto_increment"
my_cursor.execute(q_alter)

"""Describe a table"""
q_describe="Describe customers"
my_cursor.execute(q_describe)
for x in my_cursor:
	print(x)

"""Insert a raw in a table"""
q_insert = "INSERT into customers(name,address, city) values (%s,%s,%s)"
data = [('Yassine',"4 avenue Pierre semard","villiers-le-bel"),
		('Amine',"15 avenue Pierre semard","Gonesse"),
		('Lam',"20 avenue Pierre semard","Paris"),
		]

"""Drop a column"""
q_drop = "ALTER table customers drop column id"
my_cursor.execute(q_drop)
"""obligatoire apres insert"""
db.commit()


my_cursor.execute(q_insert,('Yassine',"4 avenue Pierre semard","villiers-le-bel"))
for item in data :
	my_cursor.execute(q_insert,item)
db.commit()
print(mycursor.rowcount, "record inserted.")


"""Select"""
q_select = "select * from customers"
my_cursor.execute(q_select)
for x in my_cursor:
	print(x)

"""obligatoire apres delete"""
db.commit() 

"""delete a raw in a table"""
q_delet = "delete from customers where id = 10"
my_cursor.execute(q_delet)


"""EXECUTEMANY"""
other_data = [('Kamilia',"21 avenue Pierre semard","Arnouville"),
			  ('Basma',"64 avenue Pierre semard","Sarcelles"),
			]
my_cursor.executemany(q_insert,other_data)
db.commit()
print(my_cursor.rowcount, "record inserted.")

my_cursor.execute(q_select)
#Note: We use the fetchall() method, which fetches all rows from the last executed statement.
b = my_cursor.fetchall()
for x in b:
	print(x)

"""WHERE"""
q_where = "select * from customers where city = 'Gonesse'"
my_cursor.execute(q_where)
for x in my_cursor:
	print(x)


q_wildcar = "select * from customers where city like '%way%'"
my_cursor.execute(q_wildcar)
for x in my_cursor:
	print(x)


q_order = "select * from customers order by name desc"
my_cursor.execute(q_order)
for x in my_cursor:
	print(x)


q_cre_table = "CREATE TABLE test(name varchar(50), address varchar(100))"
my_cursor.execute(q_cre_table)

"""Delete a table"""
q_delete_table = "drop table test"
my_cursor.execute(q_delete_table)
db.commit()

"""Delete a table if it exists"""
q_delete_table = "drop table if exists test"
my_cursor.execute(q_delete_table)
db.commit()


"""update a column"""
q_update = "update customers set address = 'Valley 345' where address ='4 avenue Pierre semard'"
my_cursor.execute(q_update)
db.commit()

"""limit + offset"""
q_select_limit = "select * from customers limit 3 offset 2"
my_cursor.execute(q_select_limit)
b = my_cursor.fetchall()
for x in b:
	print(x)


q1 = "create table users(id int PRIMARY KEY auto_increment, name varchar(50), fav int, Foreign key(fav) references products(id))"
my_cursor.execute(q1)

q1 = "create table products(id int PRIMARY KEY auto_increment, name varchar(50))"
my_cursor.execute(q1)

q1 = "drop table users"
my_cursor.execute(q1)

q1 = "create table products(id int PRIMARY KEY auto_increment, Foreign key(id) references users(fav), name varchar(50))"
my_cursor.execute(q1)

q_insert = "INSERT into products(name) values (%s)"

q_insert = "INSERT into users(name) values (%s)"

data_users = [
			('Yassine','1'),
			('Amine','2'),
			('Lam','3'),
			('Kam','1'),
			]
data_prod = [('Chocolate Heaven',),('Tasty',),('Vanilla Dreams',)]

my_cursor.execute(q_insert,("Joe",))
db.commit()

my_cursor.executemany(q_insert,data_users)
# for item in data_prod:
# 	# my_cursor.execute(q_insert,item)
# 	print(item)
db.commit()

#Join and inner join give the same result
q = "select u.name, p.name, p.id from users u join products p where p.id = u.fav"
q = "select u.name, p.name, p.id from users u inner join products p on p.id = u.fav"

my_cursor.execute(q)
for x in my_cursor:
	print(x)


q = "select u.name, p.name from users u left join products p on p.id = u.fav"
my_cursor.execute(q)
for x in my_cursor:
	print(x)

q = "select u.name, p.name from users u right join products p on p.id = u.fav"
my_cursor.execute(q)
for x in my_cursor:
	print(x)
