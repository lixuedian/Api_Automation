from Params.params_ht import *
import TestCase.Trading_desk
from Common.Methodes import notify, log
from Common.Parser import parser


class Role(object):
    url = TestCase.Trading_desk.url
    header = TestCase.Trading_desk.header('Trading')
    roleId = ''

    def role_list(self):
        """获取角色信息"""
        case = OauthList().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], case[0]['data'],
                                        self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])
        Role.roleId = result['data'][0]['id']

    def role_get(self):
        """根据id获取角色信息"""
        case = GetOauth().case_data
        data = {
            "roleId": Role.roleId
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def role_edit(self):
        """根据id编辑角色信息"""
        case = EditOauth().case_data
        data = {
            "roleId": Role.roleId,
            "roleName": "测试角色001",
            "note": "note"
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def delete(self):
        """'根据id删除角色信息'"""
        case = DeleteOauth().case_data
        data = {
            "roleId": Role.roleId
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def role_main(self):
        """获取角色信息"""
        Role().role_list()
        """根据id获取角色信息"""
        Role().role_get()
        """根据id编辑角色信息"""
        Role().role_edit()
        """根据角色获取对应的权限信息"""
        Role().get()
        """根据角色修改对应的权限信息"""
        Role().edit()
        """'根据id删除角色信息'"""
        Role().delete()

    def get(self):
        case = GetPermissionByRole().case_data
        """根据角色获取对应的权限信息"""
        data = {
            "roleId": Role.roleId
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def edit(self):
        """根据角色修改对应的权限信息"""
        data = {
            "roleId": Role.roleId,
            "permissionIds": "181,182,183,184,192,41,42,43"
        }
        case = PrDelePermissionByRole().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])


class PermissionS(object):
    url = TestCase.Trading_desk.url
    header = TestCase.Trading_desk.header('Trading')
    permissionId = ''

    def permission_get(self):
        """获取资源信息byId"""
        data = {
            "permissionId": PermissionS.permissionId,

        }
        case = PermissionGet().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def permission_edit(self):
        """根据id修改资源信息"""
        data = {
            "id": PermissionS.permissionId,
            "createTime": "2021-07-12T10:43:40.000+00:00",
            "updateTime": "2021-07-12T10:43:40.000+00:00",
            "createBy": 1099,
            "updateBy": 1099,
            "isDeleted": 0,
            "projectId": 110,
            "name": "测试功能",
            "path": "/getPermissionsByLevel001",
            "permissionLevel": 4,
            "display": 1,
            "rootId": 43,
            "rootIds": "41,42,43",
            "permissionType": 3,
            "permissionPath": "后台管理-\u003e权限系统-\u003e菜单管理",
            "rootIdList": [
                41,
                42,
                43
            ]
        }
        case = PermissionEdit().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def permission_display(self):
        """资源列表展示状态调整入口"""
        data = {
            "permissionId": PermissionS.permissionId,
            "display": "1"
        }
        case = PermissionDisplay().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def permission_delete(self):
        """资源信息删除"""
        case = PermissionDelete().case_data
        data = {
            "permissionId": PermissionS.permissionId
        }
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], data, self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

    def func_list(self):
        """功能列表"""
        case = FuncList().case_data
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        result = notify().notify_result(case[0]['mode'], self.url + case[0]['url'], case[1]['data'],
                                        self.header, case[0]['type'])
        log.info('响应结果：%s' % result)
        parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])
        try:
            PermissionS.permissionId = result['data']['list'][0]['id']
        except IndexError:
            PermissionS.permissionId = ''

    def permission_main(self):
        PermissionS().func_list()
        PermissionS().permission_get()
        PermissionS().permission_edit()
        PermissionS().permission_display()
        PermissionS().permission_delete()
