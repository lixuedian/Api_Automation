
import allure
import pytest
from Common import Consts
from Params.params_ht import *
from Params.params_department import *
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_mp import Role, PermissionS

url = TestCase.Trading_desk.url
header = TestCase.Trading_desk.header()
BASE_PATH = TestCase.BASE_PATH


class TestDepartment(object):

    @allure.description('获取部门的树状结构')
    @pytest.mark.parametrize('case', DepartmentList().case_data)
    def test_department_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('更新部门备注')
    @pytest.mark.parametrize('case', DepartmentUpdate().case_data)
    def test_department_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('查询该部门下的员工,分页')
    @pytest.mark.parametrize('case', DepartmentUser().case_data)
    def test_department_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('通过各种查询条件查询用户，单条')
    @pytest.mark.parametrize('case', GetUser().case_data)
    def test_department_04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('更新用户备注,状态，业务线')
    @pytest.mark.parametrize('case', Update().case_data)
    def test_department_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('多条件组合查询该部门下员工，多条')
    @pytest.mark.parametrize('case', GetUserList().case_data)
    def test_department_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('判断某条业务线是否在用')
    @pytest.mark.parametrize('case', IsBussinessInUse().case_data)
    def test_department_07(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('根据部门获取已绑定相关角色')
    @pytest.mark.parametrize('case', RoleLIst().case_data)
    def test_department_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取部门下可添加的角色')
    @pytest.mark.parametrize('case', GetUsableRole().case_data)
    def test_department_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('给部门添加角色')
    @pytest.mark.parametrize('case', AddDepartment().case_data)
    def test_department_10(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('禁用、启用用户角色')
    @pytest.mark.parametrize('case', Status().case_data)
    def test_department_11(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('从部门下删除角色')
    @pytest.mark.parametrize('case', DelRoleDepartment().case_data)
    def test_department_12(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestRole(object):

    @allure.description('添加角色')
    @pytest.mark.parametrize('case', RoleAdd().case_data)
    def test_role_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])

        Role().role_main()

        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    # @allure.description('获取角色信息')
    # @pytest.mark.parametrize('case', OauthList().case_data)
    # def test_role_06(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')
    #     return TestRole.roleId == result['data'][0]['id']
    #
    # @allure.description('根据id获取角色信息')
    # @pytest.mark.parametrize('case', GetOauth().case_data)
    # def test_role_07(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')
    #
    # @allure.description('根据id编辑角色信息')
    # @pytest.mark.parametrize('case', EditOauth().case_data)
    # def test_role_08(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')
    #
    # @allure.description('根据id删除角色信息')
    # @pytest.mark.parametrize('case', DeleteOauth().case_data)
    # def test_role_09(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')


class TestPermission(object):

    @allure.description('添加菜单权限')
    @pytest.mark.parametrize('case', MenuAdd().case_data)
    def test_permission_10(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('菜单列表')
    @pytest.mark.parametrize('case', MenuList().case_data)
    def test_permission_15(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('添加功能权限')
    @pytest.mark.parametrize('case', FuncAdd().case_data)
    def test_permission_16(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        PermissionS().permission_main()
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('功能列表')
    @pytest.mark.parametrize('case', FuncList().case_data)
    def test_permission_17(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('指定获取几级菜单')
    @pytest.mark.parametrize('case', GetPermissionsByLevel().case_data)
    def test_permission_18(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestUserRole(object):

    @allure.description('给用户添加自定义角色')
    @pytest.mark.parametrize('case', UserRoleAdd().case_data)
    def test_user_role_19(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取用户角色列表')
    @pytest.mark.parametrize('case', UserRoleList().case_data)
    def test_user_role_20(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取用户可用角色列表')
    @pytest.mark.parametrize('case', UserGetUsableRole().case_data)
    def test_user_role_21(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    # @allure.description('根据角色获取对应的权限信息')
    # @pytest.mark.parametrize('case', GetPermissionByRole().case_data)
    # def test_user_role_23(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')
    #
    # @allure.description('根据角色修改对应的权限信息')
    # @pytest.mark.parametrize('case', PrDelePermissionByRole().case_data)
    # def test_user_role_24(self, case):
    #     log.info("*************** 开始执行用例 ***************")
    #     log.info("用例名称  ==>> {}".format(case['test_name']))
    #     result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
    #     log.info('响应结果：%s' % result)
    #     parser(result, case['test_name'], case['parser'], case['expected'])
    #     allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
    #     Consts.RESULT_LIST.append('True')

    @allure.description('删除用户自定义角色')
    @pytest.mark.parametrize('case', UserRoleDelete().case_data)
    def test_user_role_25(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
