# encoding:utf-8
__author__ = 'jian.chen'


import unittest
import os,sys,time
os.path.append('c:\\move')
from PO import takeshot
from Data import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class openBox(unittest.TestCase):
    def setUp(self):
        devices = config.idol
        self.driver = config.idol.driver
        self.my_watch = config.idol.my_watch

    def tearDown(self):
        takeshot.home_back(self.driver)
        pass

    def test_open_box(self):

        #about app

        #about watch

        #开始配对

        takeshot.findID(self,self.driver,"start_pair")

        #跳过账号注册模块
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/sign_skip")


        #设置名称
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/setting_username_layout")
        name_text = takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/edit_profile_name")
        name_text.send_keys("test")
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/set_save")


        #设置性别
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/setting_gender_layout")
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/gender_female")
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/set_save")

        #设置身高
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/setting_height_layout")
        element1 = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/pickers")
        location1 = element1.location
        size1 = element1.size
        x11 = location1["x"] + 220
        y11 = location1["y"] + size1["height"] - 1
        x22 = x11
        y22 = location1["y"] + 1
        self.driver.swipe(x11,y11,x22,y22,500)
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/set_save")

        #设置体重
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/setting_weight_layout")
        element2 = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/pickers")
        location1 = element2.location
        size1 = element2.size
        x11 = location1["x"] + 220
        y11 = location1["y"] + size1["height"] - 1
        x22 = x11
        y22 = location1["y"] + 1
        self.driver.swipe(x11,y11,x22,y22,500)
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/set_save")

        #设置年龄
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/setting_birth_layout")
        element3 = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/pickers")
        location1 = element3.location
        size1 = element3.size
        x11 = location1["x"] + 220
        y11 = location1["y"] + size1["height"] - 1
        x22 = x11
        y22 = location1["y"] + 1
        self.driver.swipe(x11,y11,x22,y22,500)
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/set_save")

        #保存
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/save_area")
        print(takeshot.str("保存个人信息"))

        #配对手表
        takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/pair_watch_area")

        address = WebDriverWait(self.driver,60).until(lambda driver:driver.find_element_by_name(self.my_watch))
        self.assertIsNotNone(address)
        print(unicode("找到到手表","utf-8"))
        time.sleep(1)
        address.click()

        try:
            ele = WebDriverWait(self.driver,30).until(lambda driver:driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/use_watch_title"))
            spanTF = True
        except:
            spanTF = False
        if spanTF:
            msg = "配对成功"
            print (unicode(msg,'utf-8'))

            #滑动动画
            view = "com.jrdcom.wearable.smartband2:id/gif_view"
            for i in range(8):

                takeshot.swipLeft(self.driver,view)

            takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/dashboard_button")

            #设置通知
            takeshot.findID(self,self.driver,"android:id/button1")
            takeshot.findID(self,self.driver,"com.android.settings:id/checkbox")
            takeshot.findID(self,self.driver,"android:id/button1")
            self.driver.press_keycode("4")
            takeshot.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/notifications_settings_done")
            for i in range(3):
                self.driver.find_element_by_xpath("//android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]").click()
                self.driver.find_element_by_xpath("//android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[3]").click()
                self.driver.find_element_by_xpath("//android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[4]").click()
                self.driver.find_element_by_xpath("//android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]").click()
            watch_loc = WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_id("connect_status_icon"))
            self.assertIsNotNone(watch_loc)
            watch_loc.click()
            takeshot.unpair_watch(self.driver)



        else:
            msg = "配对失败"
            print (unicode(msg,'utf-8'))
            takeshot.take_shot(self.driver)
            self.assertIsNotNone(ele)

if __name__ == "__main__":
    unittest.main()










