#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost:8888",
    port = "8889",
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
    database = "Site_dyna_test",
    user = "root",
    passwd = "root"
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT category FROM Blog")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
