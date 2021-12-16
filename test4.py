import mysql.connector
from MySQL_cnx import get_cnx
from mysql.connector.errors import Error
import pandas as pd

# DB의 내용을 파이썬으로 가져오기
try :
    cnx = get_cnx()

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

except mysql.connector.Error as e:
    print('Error while connecting to MySQL\n',e)

finally :
    cursor.closed()
    if cnx.is_connected():
        cnx.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')
