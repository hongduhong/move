# -*-coding:utf-8-*-
#!usr/bin/python

__author__ = "jian.chen"


import os
import sys,time
import re

device_path = "./device_list.txt"
state_path = "./state.txt"
on_mode = False

#查找设备
os.system("adb wait-for-device")
os.system("adb devices > device_list.txt")
list = open(device_path)
device = list.read()

b = re.findall('.*device',device)

if len(b) ==1:
    print "Can't find device !"

elif len(b) ==2:
    a = b[1]
    c = re.compile('\tdevice')
    d = c.sub('',a)
    print "Get device :",d

    #初始化电池数据
    os.system("adb shell dumpsys batterystats --enable full-wake-history")
    os.system("adb shell dumpsys batterystats --reset")

    while True:
        os.system("adb shell cat /sys/class/power_supply/battery/capacity > state.txt")
        level_file = open(state_path)
        battery_level = level_file.read()
        if re.match('57',battery_level):
            print "Low power , to dump battery !"
            on_mode = True
            break
        else:
            print "Battery Level :",battery_level
            time.sleep(60)
            continue

if on_mode:
    os.system("adb bugreport > bugreport.txt")
    print "Get bugreport suscessful."



"""
if r1.search(list):
    print 'Get device!'
    print list
    os.system("adb shell cat /sys/class/power_supply/battery/capacity > state.txt")

else:
    print "Can't find device !"
"""


