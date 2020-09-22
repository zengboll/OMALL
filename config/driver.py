
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-14 19:03:49
# @FileName:  driver.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-15 15:48:07
'''
from appium import webdriver


class Driver():
	"""驱动类

	配置单设备的驱动类

	后续再研究和完善多设备的情况

	:param platformName: Android or iOS
	:param platformVersion: 待运行手机系统版本，命令行键入adb shell getprop ro.build.version.release获取
	:param deviceName: 设备名称，命令行键入adb devices获取
	:param appPackage: 待运行应用包名
	:param appActivity: 待运行应用MainActivity
	:param automationName: UiAutomator or UiAutomator2,UiAutomator2才能捕捉toasts
	:param noReset: 设置不再重复安装appium setting APK
	"""
	desired_caps={}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '10'
	desired_caps['deviceName'] = '6HJDU19821002290'
	desired_caps['appPackage'] = 'com.msyc.onion'
	desired_caps['appActivity'] = 'com.msyc.onion.ui.activities.MainActivity'
	desired_caps['automationName'] = 'UiAutomator2'
	desired_caps['noReset'] = True

	def get_driver(self):
		"""返回driver实例

		:return: driver
		"""
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
		return driver