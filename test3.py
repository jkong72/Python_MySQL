from logging import ERROR, error
import mysql.connector
from datetime import datetime as dt
# 여러 데이터를 insert
try :
    # DB와 연결
    cnx = mysql.connector.connect(
        host ='endpoint',
        database = 'forstreamlit',
        port =3306,
        user ='id',
        password ='pw'
    )
    # 쿼리문을 작성

    current_time = dt.now()

    query='''insert into test
            (name, created_at)
            values
            (%s, %s);  '''
    # 단일 데이터 튜플은 (요소)가 아닌 (요소,)의 형식으로 작성한다.
    # 여러 데이터를 삽입 할 때에는 리스트를 통해 건네준다.
    record = [('젤다',current_time),
            ('그린먼',current_time)]
    
    # 연결로부터 커서를 가져옴
    cursor = cnx.cursor()

    # 쿼리문을 커서에 넣어 실행. 한번에 여러 데이터를 건넬 때는 executemany이용.
    cursor.executemany(query, record)

    # 연결을 commit (DB에 반영)
    cnx.commit()

except mysql.connector.Error as e:
    print('Error ', e)
finally :
    if cnx.is_connected():
        cursor.close()  # 커서 닫음
        cnx.close()     # 연결 닫음
        print ('MySQL connection is closed')