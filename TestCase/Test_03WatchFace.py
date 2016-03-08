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


    def tearDown(self):
        pass

    def test_watch_face(self):

        try:

            common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/connect_status_icon")
            common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/watch_face_layout")

            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
            WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
            print(""" "Mood" """ "Watch face check ok.")

            #Classic


            b = 1
            for a in range(4):


                common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(14):

                    try:
                        common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                b = b +1
                time.sleep(1)

            print(""" "Classic" """ "Watch face check ok.")


            #Modern
            b = 1
            for a in range(4):

                ele1 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]"
                ele2 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b


                #Wallpaper
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(12):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                #Color
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchColor")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(2):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                b = b +1
                time.sleep(1)

            print(""" "Modern" """ "Watch face check ok.")

            #Diva

            b = 1
            for a in range(3):

                ele1 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]"
                ele2 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b


                #Wallpaper
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.swipeUp(self.driver,"com.jrdcom.wearable.smartband2:id/scroll_view")
                time.sleep(1)

                ele = self.driver.find_element_by_id("com.jrdcom.wearable.smartband2:id/showhometime_switch")
                Show = ele.get_attribute("checked")

                try:
                    self.assertEqual(Show,"true")
                    print("Show Home Time is selected")
                except:
                    common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/showhometime_switch")
                    print("BOSS,i have select it")

                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(19):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                #Color
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchColor")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(7):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                b = b +1
                time.sleep(1)

            print(""" "Diva" """ "Watch face check ok.")


            #Digital


            b = 1
            for a in range(4):

                ele1 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[5]/android.widget.ImageView[1]"
                ele2 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b


                #Wallpaper
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                time.sleep(1)
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(13):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                #Color
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchColor")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)

                for i in  range(5):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                        time.sleep(1)

                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                        time.sleep(1)

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)


                b = b +1
                time.sleep(1)

            print(""" "Digital" """ "Watch face check ok.")



            #Chronograph
            b = 1
            for a in range(2):

                ele1 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[6]/android.widget.ImageView[1]"
                ele2 = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[%s]/android.widget.ImageView[1]"%b


                #Wallpaper
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchWallpaper")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                time.sleep(1)
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                for i in  range(4):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))

                #Color
                common.clickAgain(self,self.driver,ele1,ele2)
                common.swipeToRight(self.driver,"com.jrdcom.wearable.smartband2:id/scrollViewWatchColor")
                time.sleep(1)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)

                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)


                for i in  range(13):

                    try:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                        time.sleep(1)

                    except:
                        common.clickAgain(self,self.driver,ele1,ele2)
                        common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                        common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                        WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                        time.sleep(1)


                common.clickAgain(self,self.driver,ele1,ele2)
                common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
                common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
                WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
                time.sleep(1)

                b = b +1
                time.sleep(1)


            common.clickAgain(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.GridView[1]/android.widget.FrameLayout[6]/android.widget.ImageView[1]","//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
            common.swipeUp(self.driver,"com.jrdcom.wearable.smartband2:id/scroll_view")
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/more_button")
            common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            common.findXpath(self,self.driver,"//android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
            time.sleep(1)
            ok = WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_name("OK"))
            ok.click()
            time.sleep(1)
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/cropButton")
            common.findID(self,self.driver,"com.jrdcom.wearable.smartband2:id/apply_button")
            WebDriverWait(self.driver,100).until(lambda x:x.find_element_by_id("com.jrdcom.wearable.smartband2:id/watch_style"))
            time.sleep(1)

            

            print(""" "Chronograph and take a camera photo" """ "Watch face check ok.")


        except:
            common.take_shot(self.driver)
            print(common.str("测试失败!"))
            raise Exception("Test failed")


if __name__ == "__main__":
    unittest.main()
