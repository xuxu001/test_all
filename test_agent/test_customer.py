# -*- coding:utf-8 -*-
import pymysql

class Customer(object):
    def __init__(self,conn):
        self.conn = conn
        self.i = 0
        self.a = 0

    #
    # def t_customer(self):
    #
    #     cursor = self.conn.cursor()
    #     sql ="""select * from t_customer where created_time>'2019-09-17 00:00:05'"""
    #     data = cursor.execute(sql)
    #     ress = cursor.fetchall()
    #     for res in ress:
    #         id = res[0]
    #         agent_id = res[1]
    #         phone = res[4
    #         print("id=%s,agent_id=%s,phone=%s" %
    #               (id, agent_id, phone))
    def t_xiaoe_customer(self):
        data ="'"+'2019-09-18 00:00:00'+"'"
        try:
            cursor = self.conn.cursor()
            # 小鹅当日注册用户
            sql = """select * FROM t_xiaoe_customer WHERE created_time >%s"""%(data)

            data = cursor.execute(sql)
            res = cursor.fetchall()
            print('正在检测导入用户')
            print('%s个用户需要检测'%(cursor.rowcount))
            for re in res:
                user_id = re[2]
                phone = re[3]

                print("user_id=%s,phone=%s" % (user_id, phone))
                self.is_one(phone)
            print('用户行数大于1的个数%s'%(self.i))
            print('用户未注册个数%s'%(self.a))
            print('导入用户结束')
        finally:
            cursor.close()

    def is_one(self,phone):
        cursor = self.conn.cursor()
        try:
            # 是否是只有一条
            phoner = "'" +phone +"'"


            sql_customer = 'select * from t_customer where phone = %s' % (phoner)
            data_customer = cursor.execute(sql_customer)
            rs_customer = cursor.fetchall()
            if cursor.rowcount != 1:
                print('-----------------------------------------------------------------------------------------')
                print('用户导入数据错误%s'%(phoner))
                print('------------------------------------------------------------------------------------------')
                self.i = self.i + 1
            for rs in rs_customer:
                name = rs[3]
                reg = rs[8]

                if reg !=1:
                    print('%s用户导入错误'%(name))
                    self.a = self.a + 1


        finally:
            cursor.close()



if __name__ == "__main__":
    conn = pymysql.connect(
        host="rm-bp1349z8ay2u070sfmo.mysql.rds.aliyuncs.com",
        user="read_only",
        password="7dian7fen_read_only",
        db="wxb-agent",
        charset='utf8',
        port=3306
    )

    test = Customer(conn)
    test_customer = test.t_xiaoe_customer()
    conn.close()

