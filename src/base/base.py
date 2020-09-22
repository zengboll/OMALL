
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-14 19:34:58
# @FileName:  base.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-15 18:50:22
'''

import time
import os

class Base(object):
	"""基类

	封装查找、点击、输入等函数
	"""

	def __init__(self, driver):
		"""初始化

		:param driver: 驱动实例
		"""
		self.driver = driver

	def find_element(self, loc, time_out=10):
		"""查找元素

		:param loc: 定位参数，如("id", "xxx")
		:param time_out: 超时时间
		:return: element or None
		"""
		element = None
		for i in range(time_out):
			print("查找元素:{}第{}次".format(loc, i))
			try:
				element = self.driver.find_element(*loc)
			except Exception as e:
				print("第{}次查找异常：{}".format(i, e))
				pass
			if element:
				return element
			else:
				time.sleep(1)
		return element

	def find_elements(self, loc, time_out=10):
		"""查找当前页所有元素

		:param loc: 定位参数，如("id", "xxx")
		:param time_out: 超时时间
		:return: element or []
		"""
		elements = []
		for i in range(time_out):
			print("查找所有元素：{}第{}次".format(loc, i))
			try:
				elements = self.driver.find_elements(*loc)
			except  Exception as e:
				print("第{}次查找异常：{}".format(i, e))
				pass
			if elements:
				return elements
			else:
				time.sleep(1)
		return elements

	def click(self, loc, index=0):
		"""点击

		:param loc: 定位参数，如("id", "xxx")
		:param index: 索引
		:return: None
		"""
		if index == 0:
			element = self.find_element(loc)
			if element:
				print("element:", element)
				element.click()
				time.sleep(1)
			else:
				print("点击：{}失败！".format(loc))
		else:
			elements = self.find_elements(loc)
			if elements:
				elements[index].click()
				time.sleep(1)
			else:
				print("点击：{}失败！".format(loc))
		return None

	def send_keys(self, loc, values, index=0):
		"""输入

		:param loc: 定位参数，如("id", "xxx")
		:param values: 输入的内容
		:param index: 索引
		:return: None
		"""
		if index == 0:
			element = self.find_element(loc)
			if element:
				element.send_keys(values)
				time.sleep(1)
			else:
				print("输入：{}失败！".format(loc))
		else:
			elements = self.find_elements(loc)
			if elements:
				elements[index].send_keys(values)
				time.sleep(1)
			else:
				print("输入：{}失败！".format(loc))
		return None







