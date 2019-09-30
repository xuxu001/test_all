# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

import pymysql
import time

# -*- coding:utf-8 -*-
import pymysql

class Card(object):
    def __init__(self,conn):
        self.conn = conn
        self.i = 0
        self.a = 0

    def mig_card(self):

        try:
            cursor = self.conn.cursor()
            sql = """select * from mig_card_2"""

            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                agent = re[7]
                parent = re[8]
                start = re[5]
                end = re[6]
                # print('==%s --%s'%(agent,parent))
                self.card(agent,parent,start,end)
                self.t_card_application(agent,parent,start,end)
                self.t_customer_agent(agent,start,end)


        finally:
            cursor.close()

    def card(self,agent,parent,start,end):
        try:
            cursor = self.conn.cursor()
            sql = '''select * from t_card where card_no >= '%s' and card_no <='%s' '''%(start,end)
            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                ent = re[1]
                par = re[8]
                id = re[0]
                if id ==None:
                    print('测试card失败%s'%start)
                elif ent ==agent and par == parent:
                    pass
                else:
                    print('%s中card跟新失败'% id)
        finally:
            cursor.close()

    def t_card_application(self,agent,parent,start,end):
        try:
            cursor= self.conn.cursor()
            sql = '''select * from t_card_application where  start_no>='%s' and end_no <='%s'  '''%(start,end)
            # sql = '''select * from t_card_application where  start_no ='VIPV00002472' and end_no ='VIP00002476'  '''
            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                id = re[0]
                age = re[1]
                par = re[-1]
                # print(age,par)
                if id ==None:
                    print('测试app失败%s' % start)
                elif age == par:
                    pass
                elif age == agent and par == parent:
                    pass
                else:
                    print('%s中关系表跟新失败' % id)

        finally:
            cursor.close()

    def t_customer_agent(self,agent,start,end):
        try:
            cursor = self.conn.cursor()
            sql = '''select * from t_customer_agent WHERE source_id in   (SELECT id from t_card WHERE card_no >= '%s' AND card_no <='%s' AND used_flag =1) AND settlement_type = 3'''%(start,end)
            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                age = re[2]
                id = re[0]
                if id == None:
                    print('测试AGENT失败%s' % start)
                elif age == agent:
                    pass
                else:
                    print('%s customer更新失败' %id)


        finally:
            cursor.close()


if __name__ == "__main__":
    conn = pymysql.connect(
        host="rm-bp1349z8ay2u070sfmo.mysql.rds.aliyuncs.com",
        user="read_only",
        password="7dian7fen_read_only",
        db="wxb-agent-sub-test",
        charset='utf8',
        port=3306
    )
    test = Card(conn)
    test_customer = test.mig_card()
    conn.close()

