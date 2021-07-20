import allure
import pytest
from Common import Consts
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_app102 import CatOne, AddAnswer, CatLists, GetQuestion, ClearHistory

header = TestCase.header_app
BASE_PATH = TestCase.BASE_PATH
url = TestCase.test_app102


class TestAPP102(object):
    @allure.description('001-题库-app首页 题库分类一级')
    @pytest.mark.parametrize('case', CatOne().case_data)
    def test_app102_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('002-题库-app首页-提交答案')
    @pytest.mark.parametrize('case', AddAnswer().case_data)
    def app102_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-题库-app首页 题库分类')
    @pytest.mark.parametrize('case', CatLists().case_data)
    def test_app102_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('004-题库-app首页 抽题接口')
    @pytest.mark.parametrize('case', GetQuestion().case_data)
    def test_app102_04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('005-题库-app首页-清空答题记录')
    @pytest.mark.parametrize('case', ClearHistory().case_data)
    def test_app102_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
