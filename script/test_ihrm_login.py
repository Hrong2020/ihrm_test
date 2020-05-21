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

    # 编写第一个案例，测试登录成功
    def test01_login_success(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, True, 10000, "操作成功", response, self)
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, result.get("success"))  # 断言success
        # self.assertEqual(10000, result.get("code"))  # 断言code
        # self.assertIn("操作成功", result.get("message"))  # 断言message

    def test02_mobile_is_not_exist(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000022", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test03_password_error(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002", "password": "error"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, True, 10000, "操作成功", response, self)

    def test04_mobile_is_empty(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test05_password_is_empty(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002", "password": ""}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test06_mobile_has_special_char(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "138000*0002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test07_more_params(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002", "password": "123456", "more_params": "params"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, True, 10000, "操作成功", response, self)

    def test08_less_mobile(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test09_less_password(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobile": "13800000002"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test10_none_params(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test11_error_params(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = {"mobal": "13800000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test12_None(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = None
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为:{}".format(result))

        # # 断言登录的结果
        assert_common(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response, self)


