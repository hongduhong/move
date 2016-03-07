# encoding:utf-8
__author__ = 'jian.chen'

from appium import webdriver

class idol:
	desired_caps = {}
	desired_caps ['platformName'] = 'Android'
	desired_caps ['platformVersion'] = '5.0.2'
	desired_caps ['deviceName'] = '24fc646'
	desired_caps ['appPackage'] = 'com.jrdcom.wearable.smartband2'
	desired_caps ['appActivity'] = 'com.jrdcom.wearable.smartband2.ui.activities.WelcomeActivity'
	desired_caps ['unicodeKeyboard'] = True
	desired_caps ['resetKeyboard'] = True

	my_watch = "DF:62:CB:2E:F3:42"

	driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

