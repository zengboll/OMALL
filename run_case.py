
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-14 17:46:59
# @FileName:  run_case.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-28 18:34:59
'''

import os
import time
import pytest
import allure

if __name__ == '__main__':
	#pytest.main(['-s','test_case/test_home_page.py'])
	print(">>正在执行用例，请等待...")
	pytest.main(['--alluredir', './allure_data'])
	time.sleep(3)
	print(">>正在生成报告，请等待...")
	os.system('allure generate ./allure_data -o ./report --clean')
	time.sleep(3)
	print(">>正在启动本地allure服务，请等待...")
	os.system(f'allure serve "D:\\SublimeWorkSpace\\OMALL\\allure_data"')
