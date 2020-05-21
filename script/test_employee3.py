# 导包
import logging
import unittest
import requests

import app
from api.emp_api import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common

# 创建测试类
import unittest


class TestIHRMEmployee3(unittest.TestCase):

    # 初始化函数
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_api = TestEmployeeApi()
        self.login_api = TestLoginApi()

    # 销毁函数
    def tearDown(self):
        pass

    def test01_login(self):
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("登录的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        app.Headers = headers
        # 打印令牌
        logging.info("令牌:{}".format(app.Headers))

    def test02_add_emp(self):
        response = self.emp_api.add_emp(app.Headers, "大西瓜5566123", "13768596542")
        # 打印添加的结果
        logging.info("添加员工的结果为:{}".format(response.json()))
        # 提取添加员工中的id
        app.EMP_id = response.json().get("data").get("id")
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    def test03_search_emp(self):
        # 查询员工
        # 发送查询员工的请求
        response = self.emp_api.query_emp(app.EMP_id, app.Headers)
        logging.info("查询员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    def test04_update_emp(self):

        # 修改员工
        # 发送修改员工的请求
        response = self.emp_api.modify_emp(app.EMP_id,
                                           app.Headers,
                                           "小西瓜啦啦啦啦")
        # 打印修改的结果
        logging.info("修改员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)


    def test05_delete_emp(self):
        # 删除员工
        # 发送删除员工的请求
        response = self.emp_api.delete_emp(app.EMP_id, app.Headers)
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)
