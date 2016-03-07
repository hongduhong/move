# encoding:utf-8
__author__ = "jian.chen"

import os, sys
import time
from PO import common
from Data import config
import unittest
from selenium.webdriver.support.ui import WebDriverWait



class OpenBox(unittest.TestCase):
    def setUp(self):
        self.driver = config.idol.driver
        devices = config.idol

    def tearDown(self):
        pass

    def test_watch_face(self):
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/connect_status_icon")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/watch_face_layout")

        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

        #Classic

        b = 1
        for a in range(5):


            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
            common.swiptToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
            time.sleep(2)
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b) .click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
            WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b).click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
            WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


            for i in  range(14):

                try:
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b).click()
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                    common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                    WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                except:
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b).click()
                    common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                    common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                    WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))



            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b).click()
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
            WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

            b = b +1


if __name__ == "__main__":
    unittest.main()
