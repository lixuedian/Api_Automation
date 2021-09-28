
import allure
import pytest
from Common import Consts
from Params.params_sms import *
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Common.Mysql_operate import MysqlDb


header = TestCase.H_header
BASE_PATH = TestCase.BASE_PATH
url = TestCase.test_sms_url


class TestSMS(object):

    @allure.description('获取短信任务列表')
    @pytest.mark.parametrize('case', GetMassSmsTaskList().case_data)
    def test_department_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('添加短信任务')
    @pytest.mark.parametrize('case', AddMassSmsTaskOne().case_data)
    def test_department_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestBlacklist(object):
    url = TestCase.test_user_url

    @allure.description('获取免扰用户列表')
    @pytest.mark.parametrize('case', GetNonuseUserList().case_data)
    def test_blacklist_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], self.url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('删除单条免扰用户')
    @pytest.mark.parametrize('case', DelNonuseUserOne().case_data)
    def test_blacklist_02(self, case):
        DB_CONF = TestCase.config.mysql_conf('mysql_comprehensive')
        mysql = 'update gk_ucenter.kg_nonuse_user set isDeleted=0 where username = 18600531753 and id=6'
        MysqlDb(DB_CONF).select_db(mysql)
        data = {
            'id': 6
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], self.url + case['url'], data, header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
