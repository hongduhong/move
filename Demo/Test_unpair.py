# encoding:utf-8
__author__ = 'jian.chen'

import unittest
import os,sys,time
sys.path.append('c:\\Move')
from PO import takeshot
from Data import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class unpair(unittest.TestCase):
	def setUp(self):
		self.devices = config.idol
		self.driver = config.idol.driver
		self.my_watch = config.idol.my_watch

	def tearDown(self):
		takeshot.home_back(self.driver)
		pass

	def test_unpair(self):

		meau_loc = WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_id("main_menu_list"))
		self.assertIsNotNone(meau_loc)
		meau_loc.click()

		home_loc = self.driver.find_element_by_id("menu_list_dashboard_layout")
		home_loc.click()

		watch_loc = WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_id("connect_status_icon"))
		self.assertIsNotNone(watch_loc)
		watch_loc.click()

		try:
			self.driver.find_element_by_id("pair_watch_area").is_displayed()
			paired = False
		except:
			WebDriverWait(self.driver,120).until(lambda driver:driver.find_element_by_id("find_watch_button"))
			paired = True

		if paired == False:
			connect_your_watch = self.driver.find_element_by_id("pair_watch_area")
			connect_your_watch.click()

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
			else:
				print (unicode("搜索失败","utf-8"))
				takeshot.take_shot(self.driver)
				self.assertIsNotNone(search_watch)

			try:
				WebDriverWait(self.driver,25).until(lambda driver:driver.find_element_by_id("find_watch_button").is_displayed())
				spanTF = True
			except:
				spanTF = False
			if spanTF:
				msg = "配对成功"
				print (unicode(msg,'utf-8'))
				takeshot.unpair_watch(self,self.driver)

			else:
				msg = "配对失败"
				print (unicode(msg,'utf-8'))
				takeshot.take_shot(self.driver)
				self.assertIsNotNone(self.driver.find_element_by_id("find_watch_button"))

		elif paired == True:
			takeshot.unpair_watch(self,self.driver)
		else:
			#调试打印信息代码
			msg2 = ("重连失败")
			print(takeshot.str(msg2))
			takeshot.take_shot(self.driver)
			self.assertIsNotNone(self.driver.find_element_by_id("find_watch_button"))


if __name__ == "__main__":
	unittest.main()
