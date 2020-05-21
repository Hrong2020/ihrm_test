# 1 我们先用设计模式实现ihrm登录
# 2 根据我们设计模式的实现，封装ihrm登录接口
# 3 根据封装的接口，优化ihrm登录的代码

# 导包
import unittest
import logging

import requests
from parameterized import parameterized

import app
from api.login_api import TestLoginApi
from utils import assert_common, build_data


# 创建测试类，继承unittest.TestCase


class TestIHRMLogin(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.login_api = TestLoginApi()

    def tearDown(self):
        ...

    filename = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(build_data(filename))
    # 编写第一个案例，测试登录成功
    def test_login(self, name, jsonData, http_code, success, code, message):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(http_code, success, code, message, response, self)
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, result.get("success"))  # 断言success
        # self.assertEqual(10000, result.get("code"))  # 断言code
        # self.assertIn("操作成功", result.get("message"))  # 断言message
