import sqlite3
from pathlib import Path


def insertSingleChoose(question, answer, choicea, choiceb, choicec, choiced, rawnumber):
    # INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
    sqltext = "INSERT INTO ques_choose VALUES(" + \
              "'" + question + "', " + \
              "'" + answer + "', " + \
              "'" + choicea + "', " + \
              "'" + choiceb + "', " + \
              "'" + choicec + "', " + \
              "'" + choiced + "', " + \
              rawnumber + ");"
    try:
        cur.execute(sqltext)
        con.commit()
    except sqlite3.IntegrityError:
        print('数据已存在,录入下一个')
    else:
        print(sqltext)


def insertSingleCheck(question, answer, rawnumber):
    # INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
    sqltext = "INSERT INTO ques_check VALUES(" + \
              "'" + question + "', " + \
              "'" + answer + "', " + \
              rawnumber + ");"
    try:
        cur.execute(sqltext)
        con.commit()
    except sqlite3.IntegrityError:
        print('数据已存在,录入下一个')
        return
    else:
        print(sqltext)


def readFiles():
    # 遍历文件夹下所有txt文件
    path = Path('./data/')
    filenames = []
    for file in path.rglob('*.txt'):
        filenames.append(str(file))
    # print(fileNames)

    # 所有文件的循环
    for txtfile in filenames:
        # 读取一个文件中的数据
        with open(txtfile, 'r', encoding='UTF-8') as f:
            print('读入文件:', txtfile)
            lines = f.readlines()

            for i in range(len(lines)):
                # 删除首尾无用符号
                lines[i] = lines[i].strip('\t\n')
                lines[i] = lines[i].strip('\n')
                lines[i] = lines[i].strip('\t')
                lines[i] = lines[i].strip()
                # 替换全角符号为半角
                # lines[i] = lines[i].replace(',', '，')
                # lines[i] = lines[i].replace('.', '。')
                # lines[i] = lines[i].replace('"', '”')
                # lines[i] = lines[i].replace("'", '”')

            # print(lines)
            # return
            # 所有数据都读入到lines了，开始处理数据
            count = 0
            i = 0
            while i < len(lines):
                count += 1
                if count <= 20:  # 选择题
                    # i+1=ques i+2=a i+3=aa i+4=b i+5=bb i+6=c i+7=cc
                    _ques = lines[i + 1]
                    _a = lines[i + 2]
                    _aa = lines[i + 3]
                    _b = lines[i + 4]
                    _ab = lines[i + 5]
                    _c = lines[i + 6]
                    _ac = lines[i + 7]
                    _d = ''
                    _ad = ''
                    _ans = ''
                    # a b c 不一定有 d
                    item = lines[i + 8]
                    if item[0:1] == 'D':
                        _d = lines[i + 8]
                        _ad = lines[i + 9]
                        _ans = lines[i + 10]
                        _ans = _ans[len(_ans) - 1:len(_ans)]
                        i += 11
                    elif item[0:4] == '正确答案':
                        _ans = lines[i + 8]
                        _ans = _ans[len(_ans) - 1:len(_ans)]
                        i += 9
                    insertSingleChoose(_ques, _ans, _aa, _ab, _ac, _ad, str(count))

                # elif 21 <= count <= 30: # 判断题
                else:  # 判断题
                    _ques = lines[i + 1]
                    _ans = lines[i + 2]
                    _ans = _ans[len(_ans) - 1:len(_ans)]
                    i += 3
                    insertSingleCheck(_ques, _ans, str(count))

def printDBInfo():
    # 查询数据库一共有多少条数据
    sqltext = "SELECT COUNT(*) FROM ques_choose;"
    cur.execute(sqltext)
    result = cur.fetchone()
    print('选择题总数:', result[0])
    sqltext = "SELECT COUNT(*) FROM ques_check;"
    cur.execute(sqltext)
    result = cur.fetchone()
    print('判断题总数:', result[0])



if __name__ == '__main__':
    # 连接表
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    # 插入数据
    # insertSingleCheck('a','b','1')
    # insertSingleChoose('aa','bb','c','d','e','f','1')
    readFiles()
    print("录入完毕")
    printDBInfo()
    # 关闭
    cur.close()
    con.close()
