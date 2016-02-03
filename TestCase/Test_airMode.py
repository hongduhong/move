#encoding = utf-8
__author__ = "jian.chen"


from appium import webdriver
import os,sys,time
from appium.webdriver.connectiontype import ConnectionType
import unittest
from PO import takeshot
from Data import config


class airMode(unittest.TestCase):
    def setUp(self):
        devices = config.idol
        self.driver = config.idol.driver

    def tearDown(self):
        pass

    def test_air_mode(self):


        takeshot.findID(self,self.driver,"connect_status_icon")

        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        print("Turn on AirPlan")
        takeshot.take_shot(self.driver)

        takeshot.getNetworkStatu(self.driver)

if __name__ == "__main__":
    var = unittest.main