import mysql.connector
from MySQL_cnx import get_cnx
# 데이터를 insert
try :
    # DB와 연결
    cnx = get_cnx()
    # 자동화를 위해 변수를 이용
    name = '이름'
    age = 20
    age = int(age)
    # 쿼리문을 작성
    query='''insert into test
            (name, age)
            values
            (%s, %s);  '''
    # 단일 데이터 튜플은 (요소)가 아닌 (요소,)의 형식으로 작성한다.
    # 형식을 맞춰주지 않으면 데이터가 삽입되지 않는다. (빈 데이터, .format이나 f스트링 이용등..)
    # 
    record = (name, age)
    
    # 연결로부터 커서를 가져옴
    cursor = cnx.cursor()

    # 쿼리문을 커서에 넣어 실행
    cursor.execute(query, record)

    # 연결을 commit (DB에 반영)
    cnx.commit()

except mysql.connector.Error as e:
    print('Error ', e)
finally :
    if cnx.is_connected():
        cursor.close()  # 커서 닫음
        cnx.close()     # 연결 닫음
        print ('MySQL connection is closed')