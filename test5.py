import mysql.connector
from MySQL_cnx import get_cnx
from mysql.connector.errors import Error
import pandas as pd

# DB의 내용을 딕셔너리로 가져오기
try :
    cnx = get_cnx()
    query = '''select * from test;'''

    # select 결과를 딕셔너리로
    cursor = cnx.cursor(dictionary = True)
    cursor.execute(query)

    # select 문은 아래 내용이 필요하다.
    record_list = cursor.fetchall()
    print(record_list)

    for row in record_list :
        print('id =', row['id'])
        print('date =', row['created_at'].isoformat())
        print('name =', row['name'])
        print('age =', row['age'])
        print('-'*12)

except mysql.connector.Error as e:
    print('Error while connecting to MySQL\n',e)

finally :
    cursor.closed()
    if cnx.is_connected():
        cnx.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')
