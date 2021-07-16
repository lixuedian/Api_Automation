import json

import allure
import pytest
from Common import Consts
from Params.params_department import *
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase.ZT_token


url = TestCase.Trading_desk.url
header = TestCase.Trading_desk.header('Trading')
BASE_PATH = TestCase.BASE_PATH


class TestResetPassword(object):
    @allure.description('管理员重置密码')
    @pytest.mark.parametrize('case', ResetPassword().case_data)
    def test_department_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # TestCase.token.zt_token()
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestChangePassword(object):
    @allure.description('用户修改密码')
    @pytest.mark.parametrize('case', ChangePassword().case_data)
    def test_department_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # TestCase.token.zt_token()
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
