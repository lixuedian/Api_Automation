import allure
import pytest
from Common import Consts
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_app300 import IndexMoKao, ZhenTi, Subscribe, RankingNew, RankingList, GetZhenTiDataNew, GetZhenTiCat, \
    MoZhenTi, GetZhenTiData

header = TestCase.header_app
BASE_PATH = TestCase.BASE_PATH
url = TestCase.test_app300


class TestAPP300(object):
    @allure.description('001-模考相关V1版本-获取首页模考')
    @pytest.mark.parametrize('case', IndexMoKao().case_data)
    def test_app300_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('002-模考相关V1版本-预约模考')
    @pytest.mark.parametrize('case', MoZhenTi().case_data)
    def test_app300_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-模考相关V1版本-预约模考')
    @pytest.mark.parametrize('case', Subscribe().case_data)
    def test_app300_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-模考相关V1版本-模考大赛详情')
    @pytest.mark.parametrize('case', RankingNew().case_data)
    def test_app300_04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-模考相关V1版本-模考排行榜')
    @pytest.mark.parametrize('case', RankingList().case_data)
    def test_app300_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-模考相关V1版本-获取真题数据')
    @pytest.mark.parametrize('case', GetZhenTiDataNew().case_data)
    def test_app300_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-真题相关V1版本-阶段类型-能力分类（用于切换）')
    @pytest.mark.parametrize('case', GetZhenTiCat().case_data)
    def test_app300_07(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-真题相关V1版本-真题列表')
    @pytest.mark.parametrize('case', ZhenTi().case_data)
    def test_app300_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-真题相关V1版本-真题列表')
    @pytest.mark.parametrize('case', GetZhenTiData().case_data)
    def test_app300_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('003-真题相关V1版本-真题列表')
    @pytest.mark.parametrize('case', GetZhenTiData().case_data)
    def test_app300_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
