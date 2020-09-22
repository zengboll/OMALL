
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-16 19:53:16
# @FileName:  conftest.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-16 20:19:36
'''

import pytest
from config.driver import Driver
from src.base.base import Base

"""
统一编写和存储固件函数,如驱动初始化和清理，数据库链接和关闭，接口调用
"""


@pytest.fixture(name="driver")
def set_driver():
	"""初始化和清理驱动

	执行用例前获取driver,执行后退出driver
	"""
	driver = Driver().get_driver()
	yield Base(driver)
	driver.quit()