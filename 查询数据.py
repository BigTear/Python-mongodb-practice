import sqlite3

def insertSingleChoose(question,answer,choicea,choiceb,choicec,choiced,rawnumber):
    #INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
    sqltext = 'INSERT INTO ques_choose VALUES(' + \
              '"' + question + '", ' + \
              '"' + answer + '", ' + \
              '"' + choicea + '", ' + \
              '"' + choiceb + '", ' + \
              '"' + choicec + '", ' + \
              '"' + choiced + '", ' + \
              '' + rawnumber + '' + \
              ');'
    try:
        cur.execute(sqltext)
        con.commit()
    except sqlite3.IntegrityError:
        print('数据已存在,录入下一个')
    else:
        print(sqltext)

def insertSingleCheck(question,answer,rawnumber):
    #INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
    sqltext = 'INSERT INTO ques_check VALUES('+ \
              '"' + question + '", ' + \
              '"' + answer + '", ' + \
              '' + rawnumber + '' + \
              ');'
    try:
        cur.execute(sqltext)
        con.commit()
    except sqlite3.IntegrityError:
        print('数据已存在,录入下一个')
        return
    else:
        print(sqltext)

if __name__ == '__main__':
    # 连接表
    con = sqlite3.connect('data.db')
    cur = con.cursor()


    # 关闭
    cur.close()
    con.close()