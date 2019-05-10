import mysql.connector
db = mysql.connector.connect(host = "localhost", user  = "root", passwd = "P@nigrah1")
cur = db.cursor()
cur.execute("CREATE DATABASE BankDetails")
cur.execute("commit;")
