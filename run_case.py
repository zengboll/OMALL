
'''
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2020-09-14 17:46:59
# @FileName:  run_case.py
# @Project: SublimeWorkSpace
# @Last Modified by:   zengqiu
# @Last Modified time: 2020-09-27 19:26:35
'''

import os
import pytest
import allure

if __name__ == '__main__':
	#pytest.main(['-s','test_case'])
	pytest.main(['--alluredir', './allure_data'])
	import time
	time.sleep(5)
	os.system('allure generate ./allure_data -o ./report --clean')


