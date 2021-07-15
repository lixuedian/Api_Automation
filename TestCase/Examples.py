# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 开发工具 ： PyCharm
import os
from Common.Parser import parser

import allure
import pytest
from Common.Methodes import notify
from Config.Config import Config
from Params.params import Process
from Params.params_shijuan import ShiJuan

from Common import Log
from Common import Consts
from Common import Assert

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestProcess(object):
    config = Config()
    noti = notify()
    log = Log.MyLog()
    data = Process()
    case_data = data.case_data
    test = Assert.Assertions()
    # ids = [
    #     " 测试：{} ==>  预期结果：状态码={} ".
    #         format(case['test_name'], case['expected']) for case in case_data
    # ]
    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Process')
    @allure.issue(config.test04_unified_url)
    @allure.testcase(config.test04_unified_url)
    # @pytest.mark.flaky(reruns=3)
    # @pytest.mark.parametrize('case', case_data, ids=ids)
    @pytest.mark.parametrize('case', case_data)
    def test_process(self, case):
        TestProcess.test_process.__doc__ = case['test_name']
        self.log.info('demo, utl={}, data={}, header={}'.format(case['url'], case['data'], case['header']))
        # 判断请求方法
        result = self.noti.notify_result(case['mode'], case['url'], case['data'], case['header'])
        self.log.info('响应结果：%s' % result)
        print(result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # self.test.assert_in_text(result,case['expected']),True)
        allure.attach.file((BASE_PATH+'/Log/log.log'), '附件内容是： ' + '老王调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestShiJuan(object):
    config = Config()
    noti = notify()
    log = Log.MyLog()
    data = ShiJuan()
    case_data = data.case_data
    test = Assert.Assertions()

    @allure.feature('这里是一级标签')
    # BLOCKER = 'blocker'　　中断缺陷（客服端程序无响应，无法执行下一步骤）
    # CRITICAL = 'critical'　　临界缺陷（功能点缺失）
    # NORMAL = 'normal'　　普通缺陷（数据计算错误）
    # MINOR = 'minor'　　次要缺陷（界面错误与ui需求不符）
    # TRIVIAL = 'trivial'　　轻微缺陷（必须项无提示，或者提示不规范）
    # @allure.severity('blocker')
    @allure.story('这里是第一个二级标签')
    @allure.description('这是一个测试case')
    @allure.issue(config.test_shijian_url, name='点击我跳转')
    @allure.testcase(config.test_shijian_url)
    @pytest.mark.parametrize('case', case_data)
    def test_shi(self, case):
        TestShiJuan.test_shi.__doc__ = case['test_name']
        config = Config()
        url = config.test_shijian_url
        self.log.info('demo, utl={}, data={}, header={}'.format(url+case['url'], case['data'], case['header']))
        # 判断请求方法
        result = self.noti.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        print(case['mode'], case['url'], case['data'], case['header'])
        self.log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file((BASE_PATH+'/Log/log.log'), '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')