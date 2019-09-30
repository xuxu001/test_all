# -*- coding:utf-8 -*-

import pymysql

# -*- coding:utf-8 -*-
import pymysql

class Customer(object):
    def __init__(self,conn):
        self.conn = conn
        self.i = 0
        self.a = 0

    def mig_qrcode(self):

        try:
            cursor = self.conn.cursor()
            #所有用户的二维码
            sql = """select * from mig_qrcode_2 """

            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                #二维码id,合伙人，合伙人id，更新后id
                id = re[1]
                region = re[2]
                agentid = re[3]
                updataid = re[5]
                print('开始qrcode')
                self.qrcode(id,updataid)
                print('结束qrcode')
                print('开始t_qrcode_reveice')
                self.t_qrcode_receive(id,updataid)
                print('结束')
                print('开始报告')
                self.t_report(id,updataid)
                print('结束')
                # print('开始关系表')
                # self.t_ocustomer_agent(id,updataid)
                # print('结束')




        finally:
            cursor.close()
    def qrcode(self,id,updataid):
        '''更新qrcode表'''
        try:
            cursor = self.conn.cursor()
            #所有用户的二维码
            sql = """select * from t_qrcode where id = %s"""%(id)

            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                update = re[1]
                if update == updataid:
                    pass
                else:
                    a = 0
                    a +=a
                    print('%s二维码合伙人跟新失败'%id)


        finally:
            cursor.close()

    def t_qrcode_receive(self,id,updataid):
        '''更新t_qrcode_receive'''
        try:
            cursor = self.conn.cursor()
            #所有用户的二维码
            sql = """select * from t_qrcode_receive where qrcode_id = %s"""%(id)

            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
               update = re[1]
               bind = re[6]
               if update == updataid:
                   self.t_ocustomer_agent(id,updataid,bind)

               else:
                   a = 0
                   a += a
                   print('%s中receive跟新失败'% id)

        finally:
            cursor.close()

    def t_report(self,id,updataid):
        try:
            cursor = self.conn.cursor()
            sql = '''select * from t_report_qrcode_daily where qrcode_id=%s'''%(id)

            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:
                update = re[2]
                if update == updataid:
                    pass
                else:
                    a = 0
                    a += a
                    print('%s报告表跟新失败'% id)
        finally:
            cursor.close()

    def t_ocustomer_agent(self,id,updataid,bind):
        try:
            cursor = self.conn.cursor()
            sql = '''select * from t_customer_agent where source_id = %s '''%id
            data = cursor.execute(sql)
            res = cursor.fetchall()
            for re in res:

                update = re[2]
                bind_time = re[5]
                type = re[4]
                if type ==1 and bind >bind_time and update == updataid:
                    pass
                elif type >=2 and bind >bind_time and update != updataid:
                    pass
                else:
                    print('%s绑定关系错误'%id)



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
    test = Customer(conn)
    test_customer = test.mig_qrcode()
    conn.close()

