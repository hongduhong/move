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
import os, sys, time
from appium.webdriver.connectiontype import ConnectionType
import unittest
from PO import common
from Data import config
from appium.webdriver.common.touch_action import TouchAction


class Login(unittest.TestCase):
    def setUp(self):
        deivces = config.idol
        self.driver = config.idol.driver
        self.my_watch = config.idol.my_watch

    def tearDown(self):
        pass

    def test_login_code(self):
        # 登录界面
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/main_menu_list")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/user_nickname_text")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/login_login")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/login_forgot_password")
        EmailAdress = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/email_ed")
        EmailAdress.send_keys("562746248@qq.com")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/bt_refer")
        time.sleep(8)
        common.identifyingCode(self.driver, "com.jrdcom.wearable.smartband2:id/captcha_image_view")



if __name__ == "__main__":
    unittest.main()
