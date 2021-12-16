import mysql.connector
from mysql.connector.errors import Error
import pandas as pd

# DB의 내용을 파이썬으로 가져오기
try :
    cnx = mysql.connector.connect(
        host ='endpoint',
        database = 'forstreamlit',
        port =3306,
        user ='id',
        password ='pw'
    )

    # 조건을 지정한 select
    query = '''select * from test
                where id = %s;'''
    
    parameter = (3,)

    cursor = cnx.cursor()
    cursor.execute(query, parameter)

    # select 문은 아래 내용이 필요하다.
    record_list = cursor.fetchall()
    print(record_list)

    for row in record_list :
        print('id =', row[0])
        print('date =', row[1].isoformat())
        print('name =', row[2])
        print('age =', row[3])

except Error as e:
    print('Error while connecting to MySQL\n',e)

finally :
    cursor.closed()
    if cnx.is_connected():
        cnx.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')
