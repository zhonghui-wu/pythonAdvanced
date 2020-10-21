# -*- coding: utf-8 -*-
# @project : songQin
# @author  : nathaniel
# @file     : myLog.py
# @ide     : PyCharm
# @time    : 2020/5/6 10:17
import os
import logging


def create_logger(logPath):
    """
    创建日志对象并返回
    :param: logFilePath 日志文件路径
    :return: 日志对象
    """
    # 创建日志对象
    logger = logging.getLogger(os.path.split(logPath)[-1])
    logger.setLevel(logging.INFO)

    # 打开指定的文件并将其用作日志记录流
    fh = logging.FileHandler(logPath)
    # 定义日志输出格式
    formatter = logging.Formatter("\n\n{}\n%(asctime)s - %(name)s - %(levelname)s - %(message)s".format("=" * 100))
    fh.setFormatter(formatter)

    # 往logger中添加输出方式
    logger.addHandler(fh)
    return logger


log_path = os.path.abspath("log/views.log")
viewsLog = create_logger(log_path)
