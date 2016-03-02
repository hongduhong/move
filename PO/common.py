# -*- coding:utf-8 -*-
__author__ = 'jian.chen'
'''
# download
curl -O -L http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
# extract
tar -xzf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
# build and install
python setup.py build
sudo python setup.py install
# or install it for just you without requiring admin permissions:
# python setup.py install --user
'''
import time,os,sys
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import xlrd
from PIL import Image
import pytesseract
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
		try:
			#如果报错
			'''
			1.mkdir( path [,mode] )
			  作用：创建一个目录，可以是相对或者绝对路径，mode的默认模式是0777。
			  如果目录有多级，则创建最后一级。如果最后一级目录的上级目录有不存在的，则会抛出一个OSError。

		 	2.makedirs( path [,mode] )
			  作用： 创建递归的目录树，可以是相对或者绝对路径，mode的默认模式也是0777。
			  如果子目录创建失败或者已经存在，会抛出一个OSError的异常，Windows上Error 183即为目录已经存在的异常错误。如果path只有一级，与mkdir一样。
			  '''
			os.mkdir(fp)
			filename = fp+"/" + tm+"_"+"fail"+type

		except Exception,e:
			#报错时执行
			if os.path.exists("." + fp):
				filename = "." + fp+"/" + tm+"_"+"fail"+type
				print ("Had it!")

			else:
				os.makedirs("."+fp)
				print("Creat in parent directory")
				filename = "." + fp+"/" + tm+"_"+"fail"+type

		finally:

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

#开启蓝牙搜索
def pairWatch(self,driver,my_watch):
	#Home Page
	findID(self,driver,"connect_status_icon")
	#检查是否已配对
	try:
		WebDriverWait(driver,15).until(lambda x:x.find_element_by_id("pair_watch_area"))
		paired = False
	except:
		WebDriverWait(driver,120).until(lambda driver:driver.find_element_by_id("find_watch_button"))
		paired = True

	if paired == False:

		print(str("未配对手表"))
		driver.find_element_by_id("pair_watch_area").click()
		#检查蓝牙状态并配对
		try:
			driver.find_element_by_id("alertTitle").is_displayed()
			BLE = False
		except:
			BLE = True
		if BLE == False:
			driver.find_element_by_id("button1").click()
			print (unicode("打开蓝牙以连接手表","utf-8"))
		else:
			print (unicode("蓝牙已打开","utf-8"))


		#搜索指定手表60秒，并返回结果。
		try:
			search_watch = WebDriverWait(driver,60).until(lambda driver:driver.find_element_by_name(my_watch))
			print (unicode("找到手表","utf-8"))
			band = True
		except:
			band = False

		if band == True:
			search_watch.click()
			try:
				WebDriverWait(driver,25).until(lambda driver:driver.find_element_by_id("find_watch_button").is_displayed())
				spanTF = True
			except:
				spanTF = False
			if spanTF:
				msg = "配对成功"
				print (unicode(msg,'utf-8'))

			else:
				msg = "配对失败"
				print (unicode(msg,'utf-8'))
				self.assertIsNotNone(driver.find_element_by_id("find_watch_button"))
		else:
			print (unicode("搜索失败","utf-8"))
			self.assertIsNotNone(search_watch)

	elif paired == True:
		print(str("已配对"))

	else:
		print(str("打开应用重连失败"))





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

def getNetworkStatu(driver):
	info = {"0":"NO_CONNECTION",
			"1":"AIRPLANE_MODE",
			"2":"WIFI_ONLY",
			"4":"DATA_ONLY",
			"6":"ALL_NETWORK_ON"}
	sta = driver.network_connection
	s = "%s"%sta
	status = info.get(s)
	print(status)

def get_xls(sheet_name):
	#创建储存数组
	cls = []
	#指定参数文件位置
	xls_path = os.path.join("../Data/TestData.xls")

	#读取参数文件
	data = xlrd.open_workbook(xls_path)

	#读取sheet页
	table = data.sheet_by_name(sheet_name)

	#读取行信息
	nrows = table.nrows

	for i in range(nrows):
		if table.row_values(i)[0] != "case_name":
			cls.append(table.row_values(i))

	return cls

#获取行数
def get_case_col_num(sheet_name):

	xls_path = os.path.join("../Data/TestData.xls")

	#读取参数文件
	data = xlrd.open_workbook(xls_path)

	#读取sheet页
	table = data.sheet_by_name(sheet_name)

	#读取行信息
	nrows = table.nrows

	return nrows

def get_login_email(i):

	xls_path = os.path.join("../Data/TestData.xls")

	data = xlrd.open_workbook(xls_path)

	table = data.sheet_by_name("login")
	nrows = table.nrows

	if i <= nrows:

		e = table.col_values(1)[i]

		return e
	else:
		print("Email Out of range")

def get_login_password(i):

	xls_path = os.path.join("../Data/TestData.xls")

	data = xlrd.open_workbook(xls_path)

	table = data.sheet_by_name("login")
	nrows = table.nrows

	if i <= nrows:

		e = table.col_values(2)[i]

		return e
	else:
		print("Password Out of range")

def get_login_message(i):

	xls_path = os.path.join("../Data/TestData.xls")

	data = xlrd.open_workbook(xls_path)

	table = data.sheet_by_name("login")
	nrows = table.nrows

	if i <= nrows:

		e = table.col_values(4)[i]

		return e
	else:
		print("Message Out of range")

def text_clear(driver,text):
	#Android专用清除
	driver.keyevent(123)
	for i in range(0,len(text)):
		driver.keyevent(67)

def isnumber(text):
	#判断是否可以转换为浮
	try:
		tex = int(text)
		return tex
	except:
		return text


def identifyingCode(driver, ele):
	'''获取验证码
        （startx，xstarty）
        ---------------------------------
        |     要截取的图片范围             |
        |                                |
        ----------------------------------
								(endx,endy)
    '''
	element = driver.find_element_by_id(ele)
	location1 = element.location
	size1 = element.size
	startx = location1["x"]
	starty = location1["y"]
	endx = startx + size1["width"]
	endy = starty + size1["height"]

	screenPath = (os.getcwd() + "//screen_shot.png")
	driver.get_screenshot_as_file(screenPath)
	GetScreen = Image.open(screenPath)
	box = (startx,starty,endx,endy)
	imIndentigy = GetScreen.crop(box)

	verCodePath = (os.getcwd() + "//code.png")
	imIndentigy.save(verCodePath)
	verCode = Image.open(verCodePath)
	verCode.load()
	codeStr = pytesseract.image_to_string(verCode)
	if os.path.exists(screenPath):
		os.remove(screenPath)
	else:
		print "no such file: %s" % screenPath

	if codeStr != "":
		os.remove(verCodePath)
		print codeStr
	else:
		print "Can't get the vercode,please check your network."

	return codeStr
