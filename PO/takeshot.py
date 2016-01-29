# -*- coding:utf-8 -*-
__author__ = 'jian.chen'

import time,os,sys
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

#获取截图
def take_shot(driver):
	day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	time.strftime('%Y-%m-%d', time.localtime(time.time()))
	fp = "./Result/" + day + "/image"
	tm = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	type = ".png"
	if os.path.exists(fp):
		filename = fp+"/" + tm+"_"+"fail"+type
		print (filename)
		driver.save_screenshot(filename)
		print ("sava successful")

	else:
		filename = fp+"/" + tm+"_"+"fail"+type
		print (filename)
		driver.save_screenshot(filename)
		print("creat file,save successful")

#手表界面取消配对
def unpair_watch(self,driver):
	#获取控件大小滑动控件-----------------
	element = driver.find_element_by_class_name("android.widget.ScrollView")
	location = element.location
	size = element.size
	x1 = location["x"] + 220
	y1 = location["y"] + size["height"] - 1
	x2 = x1
	y2 = location["y"] + 1

	driver.swipe(x1,y1,x2,y2,500)

	watch_settings = driver.find_element_by_id("watch_settings_layout")
	self.assertIsNotNone(watch_settings)
	watch_settings.click()

	watch_settings_back = driver.find_element_by_id("watch_settings_back")
	self.assertIsNotNone(watch_settings_back)

	element1 = driver.find_element_by_id("scroll_view")
	location1 = element1.location
	size1 = element1.size
	x11 = location1["x"] + 220
	y11 = location1["y"] + size1["height"] - 1
	x22 = x11
	y22 = location1["y"] + 1
	driver.swipe(x11,y11,x22,y22,500)

	unpair_loc = driver.find_element_by_id("watch_unpaired_layout")
	unpair_loc.click()

	verify_loc = driver.find_element_by_id("button1")
	verify_loc.click()

	done_loc = WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_id("pair_watch_area"))
	self.assertIsNotNone(done_loc)
	msg1 = ("注销手环成功")
	print(unicode(msg1,"utf-8"))
	take_shot(driver)


def home_back(driver):

	try:
		driver.find_element_by_id("connect_status_icon").is_displayed()
		back = True
	except:
		back = False

	while back==True :
		print("find you")
		break
	else:
		driver.press_keycode("4")
		print("where are you")
		
		
def str(msg):
	
	unicode(msg,"-utf")

def findID(self,driver,ele):

	element = lambda x:x.find_element_by_id(ele)
	wait_ele = WebDriverWait(driver,15).until(element)
	self.assertIsNotNone(wait_ele)
	wait_ele.click()

def swipeLeft(driver,ele):

	element4 = driver.find_element_by_id(ele)
	location1 = element4.location
	size1 = element4.size
	y1 = location1["y"] + 100
	x1 = location1["x"] + size1["width"] - 1
	y2 = y1
	x2 = location1["x"] + 1
	driver.swipe(x1,y1,x2,y2,500)

def swipeUp(driver,ele):

	element = driver.find_element_by_id(ele)
	location1 = element.location
	size1 = element.size
	x1 = location1["x"]+100
	y1 = location1["y"] + size1["height"] -1
	x2 = x1
	y2 = location1["y"]+1
	driver.swipe(x1,y1,x2,y2,500)

def findXpath(self,driver,ele):
	element = lambda x:x.find_element_by_xpath(ele)
	wait_ele = WebDriverWait(driver,15).until(element)
	self.assertIsNotNone(wait_ele)
	return wait_ele

