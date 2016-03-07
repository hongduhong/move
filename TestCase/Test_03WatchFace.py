# encoding:utf-8
__author__ = "jian.chen"

import os, sys
import time
from PO import common
from Data import config
import unittest


class OpenBox(unittest.TestCase):
    def setUp(self):
        self.driver = config.idol.driver
        devices = config.idol

    def tearDown(self):
        pass

    def test_watch_face(self):
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/connect_status_icon")
        common.findID(self, self.driver, "com.jrdcom.wearable.smartband2:id/watch_face_layout")
