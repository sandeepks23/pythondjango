#mysql-connector

#step1 import mysql module
import mysql.connector
#step2 establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
#step3 create cursor object
cursor=db.cursor()
#execute sql queries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
#close db connection
db.close()