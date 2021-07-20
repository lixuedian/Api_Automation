# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/14 10:47
# 文件名称 ： __init__.py.py
# 开发工具 ： PyCharm
import os
from Config.Config import Config
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


config = Config()
test_sms_url = config.test_sms_url
test_sms_url = '%s%s' % ('http://', test_sms_url)
test_user_url = config.test_user_url
test_user_url = '%s%s' % ('http://', test_user_url)
token = config.h_token
test_app102 = '%s%s' % ('http://', config.get_conf('test_host', 'test_app102'))
test_app300 = '%s%s' % ('http://', config.get_conf('test_host', 'test_app300'))
test_app100 = '%s%s' % ('http://', config.get_conf('test_host', 'test_app100'))


H_header = {
    'token': token
}

header_data = config.header_data('parameter')
header_app = config.header_app('APP')
