# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/21


import logging

'''
logging.basicConfig(level=logging.DEBUG,  # 设置日志级别
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',  # 指定日志格式
                    #   时间        产生日志的文件名      产生日志的行号   日志级别       日志正文
                    datefmt='%Y-%m-%D %H:%M:%S',  # 指定日志格式
                    filename='./test.log',  # 指定日志文件的路径
                    filemode='a'  # 文件打开的方式，在指定了 filename 参数的时候
                    )

logging.debug('1')
logging.info('2')
logging.warning('3')
logging.error('4')
logging.critical('5')
'''

# 创建日志对象
logger = logging.getLogger()
# 创建一个 handLer， 用于写入日志文件
fh = logging.FileHandler('./test.log')
# 再创建一个 handLer， 用于屏幕输出
ch = logging.StreamHandler()

# 制定输出格式，相当于 basicConfig 中的 format
formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')

# 将输出格式传入处理器
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 往 logger 中添加输出方式
logger.addHandler(fh)
logger.addHandler(ch)


logger.setLevel(level=logging.DEBUG)
logger.debug('这是一个debug日志')
logger.info('这是一个info日志')
logger.warning('这是一个warning日志')
logger.error('这是一个error日志')
logger.critical('这是一个critical日志')

