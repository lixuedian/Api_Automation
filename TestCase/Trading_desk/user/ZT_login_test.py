import allure
import pytest

import TestCase
from Common import Request
from Common import Consts
from Config.Config import Config
from Params.params import log
from Params.params_login import ZTLogin, LoginC
from Params.params_ht import *
from Common.Parser import parser
from Common.Methodes import notify

url = TestCase.Trading_desk.url
BASE_PATH = TestCase.BASE_PATH
header = TestCase.Trading_desk.header('Trading')


class TestLogin(object):
    request = Request.Request()
    config = Config()

    @allure.description('用户登录')
    @pytest.mark.parametrize('case', ZTLogin().case_data)
    def login_zt_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], case['header'], case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        self.config.write_configuration('Trading', result['data']['token'], str(result['data']['id']))
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('C端用户登录')
    @pytest.mark.parametrize('case', LoginC().case_data)
    def login_c_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], case['header'], case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # self.config.write_configuration('Trading', result['data']['token'], str(result['data']['id']))
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestSSO(object):
    @allure.description('sso接口，判断用户是否已登陆')
    @pytest.mark.parametrize('case', Sso().case_data)
    def test_logout_zt_02(self, case):
        data = {
            'projectId': 110,
            'token': Config().get_conf('Trading', 'token'),
            'userId': Config().get_conf('Trading', 'uuid'),
            'url': 'http://test-trade.ekeguan.com/#/login'
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], data, header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取用户具体权限')
    @pytest.mark.parametrize('case', Permission().case_data)
    def test_logout_zt_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取验证码图片')
    @pytest.mark.parametrize('case', GetVerifyCode().case_data)
    def test_logout_zt_04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


# class TestLogout(object):
#     @allure.description('交易中台用户登出')
#     @pytest.mark.parametrize('case', Logout().case_data)
#     def logout_zt_05(self, case):
#         log.info("*************** 开始执行用例 ***************")
#         log.info("用例名称  ==>> {}".format(case['test_name']))
#         result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
#         log.info('响应结果：%s' % result)
#         parser(result, case['test_name'], case['parser'], case['expected'])
#         Config().write_configuration('Trading', '', '')
#         allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
#         Consts.RESULT_LIST.append('True')
