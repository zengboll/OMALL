
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-16 19:53:16
# @FileName:  conftest.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-27 18:22:58
'''

import pytest
from config.driver import Driver
from src.base.base import Base
import allure

"""
统一编写和存储固件函数,如驱动初始化和清理，数据库链接和关闭，接口调用
"""

@pytest.fixture(name="driver")
def set_driver():
	"""初始化和清理驱动

	执行用例前获取driver,执行后退出driver
	"""
	global driver
	driver = Driver().get_driver()
	yield Base(driver)
	driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
	print("item 是什么：", item)
	print("call 是什么：", call)
	outcome = yield
	rep = outcome.get_result()
	print("rep = outcome.get_result() -->", rep)
	if rep.when == "call" and rep.failed:
		f = driver.get_screenshot_as_png()
		allure.attach(f, '失败截图', allure.attachment_type.PNG)