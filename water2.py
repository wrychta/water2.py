import mysql.connector
name = 'Wiktor'
userdate = '2020-04-03'
#connection to our remotemysql
WaterConnect = mysql.connector.connect(user='UhpGjwrwo6', password='KeeBeGzEFX',
                              host='remotemysql.com',
                              database='UhpGjwrwo6')
mycursor = WaterConnect.cursor()
sql = "SELECT SUM(howMuch) FROM " + name + " WHERE date >= '" + userdate + " 00:00:00' AND date <= '" + userdate + " 23:59:59'"
mycursor.execute(sql)
for x in mycursor:
    print(x[0])
WaterConnect.close()
'''name = 'Wiktor'
userdate = '2020-04-03'
print("SELECT * FROM " + name + " WHERE date >= '" + userdate + " 00:00:00' AND date <= '" + userdate + " 23:59:59'")'''
