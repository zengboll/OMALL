
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-03-14 19:19:45
# @FileName:  test.py
# @Project: SublimeWorkSpace
# @Last Modified by:   IT
# @Last Modified time: 2020-09-14 19:01:02

import time

from appium import webdriver


desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = '6HJDU19821002290'
desired_caps['appPackage'] = 'com.msyc.onion'
desired_caps['appActivity'] = 'com.msyc.onion.ui.activities.MainActivity'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print("start...")
time.sleep(5)
print("准备点击")
i = 0
while i < 10:
	try:
		els = driver.find_elements("id", "com.msyc.onion:id/tv_title")
	except:
		els = None
		pass
	print(els)
	if els:
		for el in els:
			try:
				print(el.text)
				if el.text == '成为会员':
					el.click()
			except:
				pass
		break
	else:
		time.sleep(1)
	i = i + 1
time.sleep(1)
AllWebView = driver.contexts
print("AllWebView:{}".format(AllWebView))
CurrentWebView = driver.context
print("CurrentWebView:{}".format(CurrentWebView))
print("切换至webView")
time.sleep(1)
driver.switch_to.context("WEBVIEW_com.msyc.onion")
CurrentWebView = driver.context
print("切换后的context:{}".format(CurrentWebView))
time.sleep(1)
el = driver.find_element("xpath", '//div[@id="sortContent"]/div/p')
print("H5页面一秒读懂：{}".format(el))
print(el.text)
print("end...")
driver.quit()
