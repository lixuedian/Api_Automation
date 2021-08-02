import allure
import pytest
from Common import Consts
from Params.params_department import *
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_user import GetTeacherByProjectCategoryId, GetTeacherByIdAndCategoryId, \
    GetTeacherByMobileAndCategoryId, SmsCode, UserSso, UserCaptcha

url = TestCase.test_trade_url
header = TestCase.zt_header
BASE_PATH = TestCase.BASE_PATH
test_mp_url = TestCase.test_mkg_url


class TestPassword(object):
    @allure.description('管理员重置密码')
    @pytest.mark.parametrize('case', ResetPassword().case_data)
    def test_reset_password_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # TestCase.token.zt_token()
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('用户修改密码')
    @pytest.mark.parametrize('case', ChangePassword().case_data)
    def test_change_password_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # TestCase.token.zt_token()
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestTeacher(object):
    @allure.description('获取现后台该业务线下所有的老师列表')
    @pytest.mark.parametrize('case', GetTeacherByProjectCategoryId().case_data)
    def test_teacher_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取现后台该业务线下所有的老师列表')
    @pytest.mark.parametrize('case', GetTeacherByIdAndCategoryId().case_data)
    def test_teacher_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取现后台该业务线下所有的老师列表')
    @pytest.mark.parametrize('case', GetTeacherByMobileAndCategoryId().case_data)
    def test_teacher_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestUserMkg(object):
    @allure.description('c端验证码发送接口')
    @pytest.mark.parametrize('case', SmsCode().case_data)
    def test_user_msg_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], test_mp_url + case['url'], case['data'],
                                        TestCase.mkg_header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('c端鉴权接口')
    @pytest.mark.parametrize('case', UserSso().case_data)
    def test_user_msg_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        data = {
            'token': TestCase.config.get_conf('mkg', 'token')
        }
        result = notify().notify_result(case['mode'], test_mp_url + case['url'], data,
                                        TestCase.mkg_header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('c端图形验证码')
    @pytest.mark.parametrize('case', UserCaptcha().case_data)
    def test_user_msg_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], test_mp_url + case['url'], case['data'],
                                        TestCase.mkg_header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
