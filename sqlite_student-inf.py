import sqlite3
conn = sqlite3.connect('crud.db')

curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS student
    (no INT PRIMARY KEY, name VARCHAR(20), sex VARCHAR(20))''')
while True:
    print('1.학생 정보 전체 조회')
    print('2. 학생 정보 조회')
    print('3. 학생 데이터 추가')
    print('4. 학생 데이터 수정')
    print('5. 학생 데이터 삭제')
    print('6. 프로그램 종료')
    choice=int(input('선택 >>'))

    if choice==1:
        curs.execute('SELECT * FROM student')
        rows = curs.fetchall()
        if not rows:
            print('입력된 학생 데이터가 없습니다.')
        else:
            curs.execute('SELECT * FROM student')
            rows = curs.fetchall()
            print(rows)
    elif choice==2:
        no = int(input('학번 입력:'))
        curs.execute('SELECT * FROM student WHERE  no =(?)', (no,))
        rows=curs.fetchall()
        print(rows)
        if not rows:
            print('조회된 데이터가 없습니다.')
    elif choice==3:
        no=int(input('학번 입력:'))
        curs.execute('SELECT no FROM student')
        rows = curs.fetchall()
        a = 0
        for i in rows:
            for x in i:
                if x == no:
                    a = 1
                    print(no,'는 이미 등록된 학번입니다.')
        if a == 0:
            name=input('이름 입력:')
            sex=input('성별 입력:')
            ins = 'INSERT INTO student (no, name, sex) VALUES(?, ?, ?)'
            curs.execute(ins,(no, name, sex))
            print('데이터가 저장되었습니다.')
    elif choice==4:
        value=int(input('수정할 학생의 학번 입력:'))
        change=input('이름 수정:')
        curs.execute('UPDATE student SET name=(?) WHERE no =(?)', (change, value))
        sex=input('성별 입력:')
        if sex == '':
            pass
        else:
            curs.execute('UPDATE student SET sex=(?) WHERE no =(?)', (sex, value))
        print('수정이 완료되었습니다.')
    elif choice==5:
        value=int(input('삭제할 학생의 학번 입력:'))
        curs.execute('SELECT * FROM student WHERE no=(?)', (value,))
        rows = curs.fetchall()
        if not rows:
            print('해당 학번의 학생은 존재하지 않습니다.')
        else:
            curs.execute('DELETE FROM student WHERE no=(?)', (value,))
            rows = curs.fetchall()
            print('삭제하였습니다.')
    elif choice==6:
        print('프로그램을 종료합니다.')
        conn.commit()
        conn.close()
        break



