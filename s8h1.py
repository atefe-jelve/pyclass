#ATEFE-JELVE__THURSDAY14-18
#USE-DB-ADD-DATA

import sqlite3  
conn = sqlite3.connect('student.db')  
cursor = conn.cursor()

name = 'ali hasan mina kati nima nami mana'.split(" ")
age = [11 , 22 , 33 , 44 , 66 , 77, 85]
klass =['c' , 'c' , 'c' , 'c' ,'c' , 'c' ,'c']
for i in range(len(name)):
    names=name[i]
    ages=age[i]
    klasss=klass[i]
    insert_query = f'insert into student values ("{names}",{ages},"{klasss}")'
    cursor.execute(insert_query)
    conn.commit()
conn.close()