import mysql.connector

'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='K!ngdomhearts2!'
   )

my_cursor = mydb.cursor()


my_cursor.execute('CREATE DATABASE lab_server')
my_cursor.execute('SHOW DATABASES')
for x in my_cursor:
    print(x)
'''

'''
lsdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='K!ngdomhearts2!',
    database='lab_server'
   )

mcursor = lsdb.cursor()

mcursor.execute('CREATE TABLE STUDENTS (id INT AUTO_INCREMENT PRIMARY KEY, FIRST_NAME VARCHAR(255), AVG_GRADE INT')
lsdb.commit()

mcursor.execute('SHOW TABLES')
for x in mcursor:
    print(x)
    '''

'''
sqls = 'INSERT INTO STUDENTS (FIRST_NAME, AVG_GRADES) VALUES (%s, %s)'
vals = [('Dylan', 0), ('Jake', 0), 
        ('Steven', 0), ('Tesoro', 0)]
mcursor.executemany(sqls, vals)

mcursor.execute('CREATE TABLE student_grades (student_id INT AUTO INCREMENT, assignment_num INT, assignment_grade INT, assignment_num_and_student_id VARCHAR(255) PRIMARY KEY))')
lsdb.commit()

mcursor.execute('SHOW TABLES')
for x in mcursor:
    print(x)
    '''
    
'''
sql = 'INSERT INTO student_grades (student_id, assignment_num, assignment_grade, assignment_name_and_student_id) VALUES (%s,%s,%s,%s)'
vars = [(1, 1, 90, '1 & 1'), (1, 2, 85, '1 & 2'), (1, 3, 100, '1 & 3'), (1, 4, 90, '1 & 4'),
        (2, 1, 75, '2 & 1'), (2, 2, 100, '2 & 2'), (2, 3, 95, '2 & 3'), (2, 4, 80, '2 & 4'),
        (3, 1, 70, '3 & 1'), (3, 2, 90, '3 & 2'), (3, 3, 80, '3 & 3'), (3, 4, 100, '3 & 4'),
        (4, 1, 100, '4 & 1'), (4, 2, 65, '4 & 2'), (4, 3, 100, '4 & 3'), (4, 4, 85, '4 & 4')]
mcursor.executemany(sql, vars)

lsdb.commit()
'''

'''
# To use for students 2, 3, & 4, set student_id to respective int
retrieve = 'SELECT AVG(assignment_grade) AS average FROM student_grades WHERE student_id = 1'
mcursor.execute(retrieve)
rows = mcursor.fetchall()
for i in rows:
    print('The average grade is: ' + str(i[0]))
    
lsdb.commit()
'''

'''
insertion = 'INSERT INTO students (AVG_GRADE) VALUES (%s)'
var = (average)
mcursor.execute(insertion, var)

lsdb.commit()
'''