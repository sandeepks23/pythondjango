import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
# sql="create table employee2(eid int,ename varchar(50),desig varchar(50),salary int)"
# cursor.execute(sql)
#
# db.close()

# sql="insert into employee2(eid,ename,desig,salary) values(100,'arun','developer','25000')"
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close()

# sql="update employee2 set salary=27000 where eid=100"
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close()
f=open("employee","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee2(eid,ename,desig,salary) values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()