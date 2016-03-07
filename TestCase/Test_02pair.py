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


			common.findXpath(self,self.driver,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("alertTitle").is_displayed()
				BLE = False
			except:
				BLE = True
			if BLE == False:
				self.driver.find_element_by_id("button1").click()
				print (unicode("打开蓝牙以连接手表","utf-8"))
			else:
				print (unicode("蓝牙已打开","utf-8"))


			#搜索指定手表60秒，并返回结果。
			try:
				search_watch = WebDriverWait(self.driver,60).until(lambda driver:driver.find_element_by_name(self.my_watch))
				print (unicode("找到手表","utf-8"))
				band = True
			except:
				band = False

			if band == True:
				search_watch.click()
				try:
					WebDriverWait(self.driver,60).until(lambda driver:driver.find_element_by_id("gif_view").is_displayed())
					spanTF = True
				except:
					spanTF = False
				if spanTF:
					msg = "配对成功"
					print (unicode(msg,'utf-8'))

				else:
					msg = "配对失败"
					print (unicode(msg,'utf-8'))
					raise Exception("pair failed")

				while 1:
					try:
						self.driver.find_element_by_id("dashboard_button")
						a = True
					except:
						a = False

					if a == True:

						print(common.str("找到你了.小杨"))
						break
					else :
						common.swipeLeft(self.driver,"gif_view")
						continue

				common.findID(self,self.driver,"dashboard_button")
				common.findID(self,self.driver,"button1")

				box = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Move")')
				box.click()
				common.findID(self,self.driver,"button1")
				os.system("adb shell input keyevent 4")
				common.findID(self,self.driver,"notifications_settings_done")

			else:
				print (unicode("搜索失败","utf-8"))
				self.assertIsNotNone(search_watch)
		except:
			common.take_shot(self.driver)
			print(common.str("测试失败"))
			raise Exception("Test failed")



if __name__ == "__main__":
	unittest.main()










