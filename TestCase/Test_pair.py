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

class pair(unittest.TestCase):
	def setUp(self):
		devices = config.idol
		self.driver = config.idol.driver
		self.my_watch = config.idol.my_watch

	def tearDown(self):
		takeshot.home_back(self.driver)
		pass

	def test_pair(self):
		watch_loc = WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_id("connect_status_icon"))
		self.assertIsNotNone(watch_loc)
		watch_loc.click()

		connect_your_watch = self.driver.find_element_by_id("pair_watch_area")
		self.assertIsNotNone(connect_your_watch)
		connect_your_watch.click()

		watch_address = WebDriverWait(self.driver,60).until(lambda driver:driver.find_element_by_name(self.my_watch))
		self.assertIsNotNone(watch_address)
		print(unicode("找到到手表","utf-8"))
		time.sleep(1)
		watch_address.click()

		try:
			ele = WebDriverWait(self.driver,30).until(lambda driver:driver.find_element_by_id("find_watch_button"))
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			msg = "配对成功"
			print (unicode(msg,'utf-8'))
		else:
			msg = "配对失败"
			print (unicode(msg,'utf-8'))
			takeshot.take_shot(self.driver)
			self.assertIsNotNone(ele)

if __name__ == "__main__":
	unittest.main()

