import sqlite3
import webbrowser
from pywebio import start_server
from pywebio.output import *
from pywebio.pin import *


def checkKeywords(keywords):
    # 删除sql语句中的特殊字符
    result = keywords.strip()

    return result


# 根据关键词查询数据库
def searchDB(table_name, keywords):
    #return [('以下关于用电常识说法错误的是 （）（2.5分）',
    # 'B',
    # '电源裸露部分应有绝缘装置', '可用试电笔去试高压电', '不用潮湿的手接触电器', '如有人触电，应迅速切断电源，然后进行抢救',
    # 8), (
    # '实验室仪器设备用电或线路发生故障着火时，应立即（ ） ，并组织人员用灭火器进行灭火。（2.5分）',
    # 'C', '将人员疏散', '将贵重仪器设备迅速转移', '切断现场电源', '', 20)]
    try:
        cur.execute("select * from " + table_name + " where 问题 like '%" + keywords + "%'")
        result = cur.fetchall()
    except sqlite3.OperationalError:
        result = ()
    return result

def main():
    with use_scope("search-area"):
        put_row([
            put_select("select_type", options=["选择题", "判断题"]),
            put_input("input_keywords", placeholder="输入题目关键词", type="text"),
        ], size="15% 85%")

    while True:
        pin_wait_change("input_keywords")
        keywords = checkKeywords(pin['input_keywords'])
        if keywords != "":
            with use_scope("result", clear=True):
                #print(pin['input_keywords'])
                # 获取到了题型和要查询的关键词
                if pin["select_type"] == "选择题":
                    result_list = searchDB("ques_choose", checkKeywords(pin["input_keywords"]))
                    for item in result_list:
                        if item[1] == 'A':
                            ans = item[2]
                        elif item[1] == 'B':
                            ans = item[3]
                        elif item[1] == 'C':
                            ans = item[4]
                        elif item[1] == 'D':
                            ans = item[5]
                        put_code("问："+item[0]+"\n答："+ans+"("+item[1]+")")

                elif pin["select_type"] == "判断题":
                    result_list = searchDB("ques_check", checkKeywords(pin["input_keywords"]))
                    for item in result_list:
                        put_code("问："+item[0]+"\n答："+item[1])
                else:
                    pass


if __name__ == "__main__":
    # 连接表
    con = sqlite3.connect("data.db", check_same_thread=False)
    cur = con.cursor()

    webbrowser.open_new_tab("http://localhost:8088")
    start_server(main, port=8088, debug=True)

    # 关闭
    cur.close()
    con.close()
