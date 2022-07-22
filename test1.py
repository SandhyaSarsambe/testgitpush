import mysql.connector as connection
mydb = connection.connect(host = 'localhost', user = 'root', passwd = 'sandhya0503')
print(mydb)