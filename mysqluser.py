#!/usr/bin/env python
import pandas as pd
import MySQLdb
host = 'localhost'
user = 'vanesa'
passwd = 'tostostos'
mydb = MySQLdb.connect(host, user, passwd)
cursor = mydb.cursor()
xl = pd.ExcelFile('NilaiMingguan/Data.xlsx')
df = xl.parse("Sheet1")
arr = df.values
for i in range(1,39):
  try:
    #dropuser = "DROP USER 'm%0.f'@'localhost';" % arr[i][1]
    #cursor.execute(dropuser)
    createuser = "CREATE USER 'm%.0f'@'localhost' IDENTIFIED BY '%.0f';" % (arr[i][1], arr[i][1])
    #print createuser
    cursor.execute(createuser)
    grantuser = "GRANT ALL PRIVILEGES ON * . * TO 'm%.0f'@'localhost';" % arr[i][1]
    #print grantuser
    cursor.execute(grantuser)
  except MySQLdb.Error, e:
    print e
