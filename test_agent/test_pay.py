# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
import pymysql

class Pay(object):
    def __init__(self,conn):
        self.conn = conn
        self.i = 0
        self.a = 0
        self.data = "'"+'2019-09-18 00:00:00'+"'"


    def pay_test(self):

        try:
            cursor = self.conn.cursor()
            # 小鹅当日注册用户
            sql = """SELECT a.id,a.xiaoe_id,a.username,a.phone,b.pay_way,b.price,b.bean FROM t_customer a JOIN t_xiaoe_payment b on a.xiaoe_id = b.user_id WHERE b.create_time >%s;"""%(self.data)

            data = cursor.execute(sql)
            res = cursor.fetchall()

            for re in res:
                print(re)
                id = re[0]
                xiaoe_id = re[1]
                phone = re[3]
                type = re[4]
                price=re[5]
                bean=re[6]
                if type == 2:
                    print(id,xiaoe_id,phone,type,bean,price)
                    self.test_pay_ios(id,xiaoe_id,phone,type,bean)
                else:
                    # self.test_pay_android(id,xiaoe_id,phone,type,price)
                    pass



        finally:

            cursor.close()

    def test_pay_android(self,id,xiaoe_id,phone,type,price):
        try:
            cursor = self.conn.cursor()
            sql = """"""
            data = cursor.execute(sql)
            res=cursor.fetchall()
            pass
        finally:
            cursor.close()

    def test_pay_ios(self,id,xiaoe_id,phone,type,bean):
        xiaoe_ids = "'"+ xiaoe_id+"'"
        try:
            cursor = self.conn.cursor()

            sql = """SELECT
	                    a.user_id,a.phone,a.pay_way,a.price,a.bean,b.agent_id,c.price,c.settlement_type,
	                    c.settlement_detail_id,d.amount,d.os_amount,d.agent_amount,d.agent_id,d.cus_source_type,d.sub_flag
	                    FROM 
	                    t_xiaoe_payment a 
                        JOIN t_customer b on a.user_id = b.xiaoe_id
                        JOIN t_payment c on b.id = c.customer_id
                        JOIN t_payment_settlement d on c.id = d.payment_id
	
                        WHERE a.created_time >%s and a.user_id=%s"""%(self.data,xiaoe_ids)

            data = cursor.execute(sql)
            res = cursor.fetchall()
            print('开始')
            for re in res:
                a =  re[0]
                print('结束')
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

    test = Pay(conn)
    test_customer = test.pay_test()
    conn.close()


