# 创建一个初始化日志的函数
import logging
import os
from logging import handlers

# 定义全局变量保存headers
Headers = None
# 保存EMP_id保存emp_id
EMP_id = None
# 定义基础路径变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def init_logging():
    # 在函数中创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器
    # 控制台处理器:将日志输出到控制台
    sh = logging.StreamHandler()
    # 文件处理器:将日志输出到文件
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='S', interval=5, backupCount=5, encoding='utf-8')
    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
