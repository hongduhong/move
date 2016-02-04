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

class airMode(unittest.TestCase):
    def setUp(self):
        devices = config.idol
        self.driver = config.idol.driver
        self.my_watch = config.idol.my_watch

    def tearDown(self):
        pass

    def test_air_mode(self):
        try:
            #检查并保持配对手环
            takeshot.pairWatch(self,self.driver,self.my_watch)

            #开启飞行模式
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
            print("Turn on AirPlan")
            takeshot.getNetworkStatu(self.driver)
            #关闭飞行模式
            time.sleep(5)
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
            print("Turn on AirPlan")
            starttime = datetime.now()

            #等待重连成功
            findWatch = WebDriverWait(self.driver,120).until(lambda x:x.find_element_by_id("find_watch_button"))
            findWatch.click()

            endtime = datetime.now()
            connectTime = endtime - starttime

            print ("Connection time : %s s" % connectTime.seconds)

        except:
            takeshot.take_shot(self.driver)
            print(takeshot.str("测试失败"))
            raise Exception("Test failed")



if __name__ == "__main__":
    unittest.main()