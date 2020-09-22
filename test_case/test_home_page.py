
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-14 16:59:05
# @FileName:  test_home_page.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-22 15:00:55
'''
import allure


@allure.feature("商城首页")
class TestHomePage():
	"""首页
	
	:param driver: 固件函数，完成setUp和tearDown，pytest自动调用conftest.py
	首页展示和跳转用例
	"""

	@allure.story("成为店主")
	@allure.title("首页进入成为店主页面")
	def test_become_member(self, driver):
		"""首页进入成为会员页
		"""
		with allure.step("1-实例化Driver"):
			driver = driver
		with allure.step("2-查找和点击首页成为会员元素"):
			loc = ("id", "com.msyc.onion:id/tv_title")
			el = driver.find_elements(loc=loc)[9]
			print(el)
			print(el.text)
			driver.click(loc=loc, index=9)
		with allure.step("3-截图"):
			pass
		with allure.step("4-断言"):
			assert 1 == 1

