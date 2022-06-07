import mysql.connector

mydb = mysql.connector.connect(
    #ipaddress
    host='localhost',
    #username
    user='root',
    #password
    password='K!ngdomhearts2!'
    #database='sakila'
    )

print(mydb)

'''mycursor = mydb.cursor()

# connect to database 

import mysql.connector

mydb  = mysql.connector.connect(
    host='localhost',
    username='root',
    password='K!ngdomhearts2'
    #database='sakila'
)'''

mycursor = mydb.cursor()

# use SQL in Python
# to run code and make changes to mySQL server
# Let's create a table with two columns: name & address
my_cursor.execute('CREATE TABLE test_table (name VARCHAR(255), address VARCHAR(255))')

# add column id as an int, and automatically increases in number and is set as primary key
my_cursor.execute('ALTER TABLE test_table ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

# Let's define variables
sql = 'INSERT INTO test_table (name, address) VALUES (%s,%s)'
val = ('Bill', '100 Bill Street')
my_cursor.execute(sql, val)

#alternative
# my_cursor.execute('INSERT INTO test_table (name, address) VALUES (%s,%s)')

# To programmatically list out your tables
my_cursor.execute('SHOW TABLES')
for x in my_cursor:
    print(x)