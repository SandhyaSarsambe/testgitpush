import mysql.connector as conn
mydb = conn.connect(host = 'localhost', user = 'root', passwd = 'sandhya0503')
cursor = mydb.cursor()
cursor.execute("insert into ")