# 导包
import logging
import unittest
import requests

# 创建测试类、继承unittest.TestCase
from api.emp_api import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common


class TestIHRMEmployee(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_api = TestEmployeeApi()
        self.login_api = TestLoginApi()

    # 销毁函数
    def tearDown(self):
        pass

    # 创建测试员工增删改查的函数
    def test01_employee_manage(self):
        # 实现员工的增删改查
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印登录的数据
        logging.info("登录的结果为：{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 打印令牌
        logging.info("请求头中令牌：{}".format(headers))

        # 添加员工
        response = self.emp_api.add_emp(headers, "拿破仑super0084", "17835793211")
        # 打印添加的结果
        logging.info("添加员工的结果为:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 查询员工
        # 发送查询员工的请求
        response = self.emp_api.query_emp(emp_id, headers)
        logging.info("查询员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 修改员工
        # 发送修改员工的请求
        response = self.emp_api.modify_emp(emp_id,
                                           headers,
                                           "贝克汉姆")
        # 打印修改的结果
        logging.info("修改员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

        # 删除员工
        # 发送删除员工的请求
        response = self.emp_api.delete_emp(emp_id, headers)
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)
