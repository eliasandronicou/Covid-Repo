import mysql.connector
from main import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)


mycursor = mydb.cursor()
#mycursor.execute("Drop DATABASE python_project;") #uncomment if Database already exists and you want to start over
mycursor.execute("CREATE DATABASE IF NOT EXISTS python_project;")
mycursor.execute("show databases")
for i in mycursor:
    print(i)

mycursor.execute("use python_project")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Months (Month VARCHAR(10),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Month,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Countries (Country VARCHAR(50),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Country,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Transport_Modes (Transport_Mode VARCHAR(50),Measure VARCHAR(5),Value BIGINT,PRIMARY KEY (Transport_Mode,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Weekdays (Weekday VARCHAR(10),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Weekday,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Commodities (Commodity VARCHAR(50),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Commodity,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Top_Months (Month VARCHAR(10),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Month,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Top_Countries (Country VARCHAR(50),Commodity VARCHAR(50),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Country,Commodity,Measure));")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Top_Day (Day VARCHAR(10),Commodity VARCHAR(50),Value BIGINT,Measure VARCHAR(5),PRIMARY KEY (Day,Commodity,Measure));")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python_project"
)
mycursor = mydb.cursor()


sql = "INSERT INTO Months (Month, Value,Measure) VALUES (%s, %s,%s)"

val = monthly_sum_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Months (Month, Value,Measure) VALUES (%s, %s,%s)"

val = monthly_sum_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Countries (Country, Value,Measure) VALUES (%s, %s,%s)"

val = country_sum_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Countries (Country, Value,Measure) VALUES (%s, %s,%s)"

val = country_sum_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Transport_Modes (Transport_Mode, Value,Measure) VALUES (%s, %s,%s)"

val = transport_sum_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Transport_Modes (Transport_Mode, Value,Measure) VALUES (%s, %s,%s)"

val = transport_sum_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Weekdays (Weekday, Value,Measure) VALUES (%s, %s,%s)"

val = weekday_sum_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Weekdays (Weekday, Value,Measure) VALUES (%s, %s,%s)"

val = weekday_sum_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Commodities (Commodity, Value,Measure) VALUES (%s, %s,%s)"

val = commodity_sum_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")


sql = "INSERT INTO Commodities (Commodity, Value,Measure) VALUES (%s, %s,%s)"

val = commodity_sum_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Months (Month, Value,Measure) VALUES (%s, %s,%s)"

val = er_6_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Months (Month, Value,Measure) VALUES (%s, %s,%s)"

val = er_6_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Countries (Country,Commodity, Value,Measure) VALUES (%s,%s, %s,%s)"

val = top_5_per_country_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Countries (Country,Commodity, Value,Measure) VALUES (%s,%s, %s,%s)"

val = top_5_per_country_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Day (Day,Commodity, Value,Measure) VALUES (%s,%s, %s,%s)"

val = best_day_a.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

sql = "INSERT INTO Top_Day (Day,Commodity, Value,Measure) VALUES (%s,%s, %s,%s)"

val = best_day_b.to_records(index=False).tolist()

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "rows were inserted.")

mycursor.close()
mydb.close()


'''
Tables 
+--------------------------+
| Tables in python_project |
+--------------------------+
| commodities              |
| countries                |
| months                   |
| top_countries            |
| top_day                  |
| top_months               |
| transport_modes          |
| weekdays                 |
+--------------------------+

'''

#export to csv files

monthly_sum_b.to_csv('er1_b.csv', index=False)
monthly_sum_a.to_csv('er1_a.csv', index=False)
country_sum_b.to_csv('er2_b.csv', index=False)
country_sum_a.to_csv('er2_a.csv', index=False)
transport_sum_b.to_csv('er3_b.csv', index=False)
transport_sum_a.to_csv('er3_a.csv', index=False)
weekday_sum_b.to_csv('er4_b.csv', index=False)
weekday_sum_a.to_csv('er4_a.csv', index=False)
commodity_sum_b.to_csv('er5_b.csv', index=False)
commodity_sum_a.to_csv('er5_a.csv', index=False)
er_6_b.to_csv('er6_b.csv', index=False)
er_6_a.to_csv('er6_a.csv', index=False)
top_5_per_country_b.to_csv('er7_b.csv', index=False)
top_5_per_country_a.to_csv('er7_a.csv', index=False)
best_day_b.to_csv('er8_b.csv', index=False)
best_day_a.to_csv('er8_a.csv', index=False)
