import allure
import pytest
from Common import Consts
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Common.Mysql_operate import mysql_select, mysql_db
from Params.params_project import AddProject, AddProjectType, GetProjectTypes, GetProjectTypeByName, \
    GetProjectListByCondition, SearchModule, GetSearch, AddProperty, EditProperty, GetOne, AddPropertyField, \
    EditPropertyField, GetPropertyField, GetOnePropertyField

header = TestCase.Trading_desk.header('Trading')
BASE_PATH = TestCase.BASE_PATH
url = TestCase.Trading_desk.url


class TestProject(object):
    # @allure.description('添加项目分类')
    # @pytest.mark.parametrize('case', AddProjectType().case_data)
    # def test_project_01(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')

    @allure.description('获取项目分类列表')
    @pytest.mark.parametrize('case', GetProjectTypes().case_data)
    def test_project_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('根据项目分类名称查询项目分类信息')
    @pytest.mark.parametrize('case', GetProjectTypeByName().case_data)
    def test_project_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    # @allure.description('添加项目')
    # @pytest.mark.parametrize('case', AddProject().case_data)
    # def test_project_04(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')

    @allure.description('根据项目分类id和名称获取项目列表')
    @pytest.mark.parametrize('case', GetProjectListByCondition().case_data)
    def test_project_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestProperty(object):
    @allure.description('字段设置列表')
    @pytest.mark.parametrize('case', SearchModule().case_data)
    def test_property_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('自定义字段列表')
    @pytest.mark.parametrize('case', GetSearch().case_data)
    def test_property_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('新增动态属性')
    @pytest.mark.parametrize('case', AddProperty().case_data)
    def test_property_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        mysql = "update test_common.property_name  set is_delete = 1  where name = 'xuejian_属性'"
        mysql_db(mysql)
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('编辑动态属性')
    @pytest.mark.parametrize('case', EditProperty().case_data)
    def test_property_04(self, case):

        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取一条动态属性的基本信息')
    @pytest.mark.parametrize('case', GetOne().case_data)
    def test_property_05(self, case):
        # mysql = "select id from test_mp_goods_center.goods_video where name = 'xuejian_组合'"
        # mysql_select(mysql)
        # data = videoId
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('新增属性字段')
    @pytest.mark.parametrize('case', AddPropertyField().case_data)
    def test_property_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        mysql = "update test_common.property_field  set is_delete = 1  where filed_name = 'xuejian_字段'"
        mysql_db(mysql)
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('编辑属性字段')
    @pytest.mark.parametrize('case', EditPropertyField().case_data)
    def test_property_07(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('查询属性字段')
    @pytest.mark.parametrize('case', GetPropertyField().case_data)
    def test_property_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取属性字段详情')
    @pytest.mark.parametrize('case', GetOnePropertyField().case_data)
    def test_property_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
