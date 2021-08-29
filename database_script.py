# -*- coding: utf-8 -*-
"""database_script

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hLfpf7WMfqH6z9VA2Zf2ji7ZC5KWUabL
"""

#Imports
import mysql.connector

DATABASE = 'Enter database link to you sql AWS Instance'
SQL = 'ENTER SQL NAME HERE'
USER = 'Enter aws user account name'
PSWRD = 'Enter aws password here'

data = mysql.connector.connect(host=DATABASE,
                             database=SQL,
                             user=USER,
                             password=PSWRD)
  
# create cursor object
cursor = data.cursor()
  
# get the sum of rows of a column
cursor.execute("SELECT * FROM ID \
                  HAVING COUNT(*) > 1;")

print('Duplicate Rows:')               
for row in cursor.fetchall(): print(row)


#Terminate connection between the database and the script

data.close()