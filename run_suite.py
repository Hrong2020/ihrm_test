# 导包
import time
import unittest
from script.test_employee3_params import TestIHRMEmployee3
from script.test_ihrm_login_params import TestIHRMLogin
# 创建测试套件


suite = unittest.TestSuite()
# 将用例集添加到测试套件中
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee3))

# 定义测试报告到指定路径文件中
# report_file = "./report" + "/IHRM_report{}.html".format(time.strftime("%Y%m%d%H%M%S"))
report_file = "./report" + "/IHRM_report.html"

# 使用HTMLTestRunner_PY3生成测试报告
with open(report_file, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    import HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=2, description="员工管理系统测试报告,很美观", title="IHRM")
    runner.run(suite)