# encoding:utf-8
__author__ = 'jian.chen'


import unittest
import os,sys,time
from PO import common
from Data import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.connectiontype import ConnectionType

class openBox(unittest.TestCase):
    def setUp(self):
        devices = config.idol
        self.driver = config.idol.driver
        self.my_watch = config.idol.my_watch

    def tearDown(self):
        pass

    def test_open_box(self):
        try:
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.Button[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()

            time.sleep(2)
            ok = WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_name("OK"))
            ok.click()
            self.driver.swipe(510,987,519,640,1000)

            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]").send_keys("juranyongdetctdexiangji")
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]").click()
            self.driver.swipe(554,784,545,1364)
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[6]").click()
            self.driver.swipe(918,767,886,1394)
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()

        except:
            common.take_shot(self.driver)
            print(common.str("测试失败"))
            raise Exception("Test failed")


if __name__ == "__main__":
    unittest.main()










