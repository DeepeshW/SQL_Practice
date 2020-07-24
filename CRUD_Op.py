# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:17:30 2020

@author: dell
"""

import mysql.connector

db = mysql.connector.connect(
        host = "localhost",
        username = "*****",
        password = "*****")

qry="INSERT INTO customers.CUSTOMER_DETAILS (ID, NAME, dob, address, Email, Phone_No, QUERY, Updated_at) \
        VALUES ('8', 'Bill', '1989/06/15', 'Street 82', 'Bill@gmail.com', '9876543219', '', '2020/07/24');"

try:
    
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("one record added successfully.")
    
except:
    
    print ("error in operation one value.")
    db.rollback()

db.close()

"""

# Insert multiple Values in database.
q1 = "INSERT INTO customers.CUSTOMER_DETAILS (ID, NAME, dob, address, Email, Phone_No, QUERY, Created_at, Updated_at) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cust_detail = [('6','Rohit','1965/02/27','Street 22','Rohit@gmail.com','6587942315','','2020/07/22','2020/07/22'),\
             ('7','Ronit','1999/09/29','Street 22','Ronit@gmail.com','2583697418','','2020/07/22','2020/07/22')]

try:
    
    cur=db.cursor()
    cur.executemany(q1, cust_detail)
    db.commit()
    print("multiple records added successfully.")
    
except:
    
    print("error in operation multiple values.")
    db.rollback()

db.close()


# Fetch records

sql = "SELECT * FROM customers.CUSTOMER_DETAILS;"

try:
    cur = db.cursor()
    cur.execute(sql)
    while True:
        record = cur.fetchone()
        
        if record == None:
            break
        print(record)

except:
    
    print ("error while fetching records.")
    db.rollback()

db.close()

# Update Record

q2 = "update customers.CUSTOMER_DETAILS set dob=%s where name=%s;"

try:
    cur = db.cursor()
    cur.execute(q2, ('1989/09/29','Ronit'))
    db.commit()
    print("Record updated successfully.")
    
except:
    
    print("error while updating record.")
    db.rollback()
    
db.close()


# Delete Record

q3 = "delete from customers.CUSTOMER_DETAILS where name=%s;"

try:
    cur = db.cursor()
    cur.execute(q3,("Sam",))
    db.commit()
    print("Record deleted successfully.")

except:
    print("error while deleting record.")
    db.rollback()
    
db.close()

"""