# -*- coding:utf-8 -*-
# coding = utf-8
import time
from selenium import webdriver

class Lunch():
    name={'壮壮','贾旭','钱克伟','童俊洁','徐磊','杨赫','胡佳音','徐向阳','马宇飞','孙益星'}
    for i in name:
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://jinshuju.net/f/brnK7T")
        driver.find_element_by_xpath('//*[@id="submission_password"]').send_keys("LSZ")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="submission_password_form"]/div/div[2]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[2]/div/div/div/div[2]/div/span/span/span/input').send_keys(i)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[4]/div/button').click()
        time.sleep(1)
        driver.quit()
        print("%s已完成报名"%i)

    print('ok')


