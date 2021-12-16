from logging import error
import mysql.connector
from mysql.connector.errors import Error

# try들여쓰기 된 코드를 실행
try :
    cnx = mysql.connector.connect(
        host ='endpoint',
        database = 'forstreamlit',
        port =3306,
        user ='id',
        password ='pw'
    )
    if cnx.is_connected() :
        db_info = cnx.get_server_info()
        print('MySQL info', db_info)
# try를 실행중 Error(조건) 가 발생하면 except문을 실행
except Error as e:
    print('Error while connecting to MySQL\n',e)
# except의 발동 여부와 관계 없이 무조건 실행하는 코드.
finally :
    if cnx.is_connected():
        cnx.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')
