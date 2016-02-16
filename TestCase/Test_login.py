# encoding:utf-8
__author__ = "jian.chen"
"""
/*****************************************************************************/
  * Filename:
  *     Test_airMode.py
  * ---------
  * Summary:
  *     切换手机飞行模式手环重连成功
  * ---------
  * Preconditions:
  *     手机与手环已连接
  * ---------
  * Setp Actions:
  *     1.进去APK,进入Watch界面
  *     2.开启手机飞行模式
  *     3.关闭手机飞行模式
  * ---------
  * Expected Result:
  *     1.进入Watch界面
  *     2.手环显示断开红色背景
  *     3.关闭后2分钟内重连手环成功
  * ---------

/*---------------------------------------------------------------------------*/
/* Comments :                                                                */
/*                                                                           */
/*===========================================================================*/
/* Modifications   (month/day/year)                                          */
/*---------------------------------------------------------------------------*/
/* date     | author     | modification                                      */
/*----------+------------+---------------------------------------------------*/
/* 04/02/16 | JianChen   | Creat Case                                        */
/*----------+------------+---------------------------------------------------*/
/*===========================================================================*/
/* Problems Report                                                           */
/*---------------------------------------------------------------------------*/
/* date     | author     | PR #     |                                        */
/*----------+------------|----------|----------------------------------------*/
/*          |            |          |                                        */
/*----------+------------|----------|----------------------------------------*/
/*          |            |          |                                        */
/*===========================================================================*/
"""

from appium import webdriver
import os,sys,time
from appium.webdriver.connectiontype import ConnectionType
import unittest
from PO import takeshot
from Data import config
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import paramunittest

loginCls = takeshot.get_login_cls()

@paramunittest.parametrized(*loginCls)

class airMode(unittest.TestCase):

    def setParameters(self,case_name,email,password,result):
        #设定参数
        self.case_name = str(case_name)
        self.email = str(email)
        self.password = str(password)
        self.resut = str(result)

    def setUp(self):
        devices = config.idol
        self.driver = config.idol.driver
        self.my_watch = config.idol.my_watch

    def tearDown(self):
        pass

    def test_login(self):


        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/main_menu_list")
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/user_nickname_text")
        #登录界面
        loginEmail = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/email_ed")
        loginEmail.send_keys(self.email)
        loginPassword = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/password_ed")
        loginPassword.send_keys(self.password)
        #登录
        self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/login_log_in")

        WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_name("Getting the user data. Please wait..."))


if __name__ == "__main__":
    unittest.main()