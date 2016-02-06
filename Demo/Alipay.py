#-*-coding:utf-8-*-
import os,time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

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
startTime = ("2016-02-06 12:26")


#获取当前时间如果是红包时间就开始抢
class go():
    try:
        while 1:
            nowTime = datetime.now().strftime("%Y-%m-%d %H:%M")
            if nowTime >= startTime:

                break
            else:
                driver.tap([(200, 1000)],500)
                time.sleep(3)
                continue

        for i in range(500):
            for y in range(10):
                driver.tap([(500, 1000)],100)

            try:
                driver.find_element_by_id("com.alipay.android.wallet.newyear:id/egg_card_close").click()
            except:
                continue

        print (unicode("完了",'-utf'))

    except:

        driver.find_element_by_id("button1").click()
        os.system("adb shell am start com.eg.android.AlipayGphone/.AlipayLogin")
        jixu = WebDriverWait(driver,15).until(lambda x:x.find_element_by_id("com.alipay.android.phone.openplatform:id/nearby_layout"))
        jixu.click()
        for i in range(500):
            for y in range(10):
                driver.tap([(500, 1000)],100)

            try:
                driver.find_element_by_id("com.alipay.android.wallet.newyear:id/egg_card_close").click()
            except:
                continue

        print (unicode("FC了，然后完了",'-utf'))

    finally:

        print("hehehehehehehehehehehehehehe")

if __name__=="__main__":
    goo = go()
    goo.run()

"""
type= point
count= 4
speed= 1.0
start data >>

Tap(500,1000)
UserWait(25)
Tap(150,400)
UserWait(25)
"""