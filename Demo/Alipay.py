#-*-coding:utf-8-*-
import os,time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


desired_caps = {}
desired_caps['deviceName'] = '24fc646'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'  #app包名
desired_caps['appActivity'] = '.AlipayLogin'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#需已登录用户
go = WebDriverWait(driver,15).until(lambda x:x.find_element_by_id("com.alipay.android.phone.openplatform:id/nearby_layout"))
go.click()

for i in range(500):
    for y in range(10):
        driver.tap([(500, 1000)],100)

    try:
        driver.find_element_by_id("com.alipay.android.wallet.newyear:id/egg_card_close").click()
    except:
        continue

print (unicode("完了",'-utf'))