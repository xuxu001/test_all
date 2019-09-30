# -*- coding:utf-8 -*-
import logging
import time
import sys
import os
now = time.strftime('%Y-%m-%d %H-%M')
#
report_path = os.path.join(os.getcwd(),'test_report')

filename = os.path.join(report_path,'api_log'+now+'.text')

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # 返回脚本的路径
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=filename,
                    filemode='wb')
logger = logging.getLogger()