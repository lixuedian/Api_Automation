import allure
import pytest
from Common import Consts
from Params.params_handout import *
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase


header = TestCase.Trading_desk.header('Trading')
BASE_PATH = TestCase.BASE_PATH
url = TestCase.Trading_desk.url


class TestHandout(object):
    @allure.description('新增讲义')
    @pytest.mark.parametrize('case', AddHandout().case_data)
    def test_handout_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('新增讲义')
    @pytest.mark.parametrize('case', AddHandout().case_data)
    def test_handout_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')