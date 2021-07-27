import os
import allure
import pytest
from Common.Methodes import notify
from Common.Parser import parser
from Config.Config import Config
from Common import Request, Log
from Common import Consts
from Common import Assert
from Params.params_login import Login, LoginK

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestBasic(object):
    log = Log.MyLog()
    data = Login()
    case_data = data.case_data
    request = Request.Request()
    test = Assert.Assertions()
    config = Config()
    noti = notify()

    # ids = [
    #     "测试：{}".
    #         format(case['test_name']) for case in case_data
    # ]
    # @allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Basic')
    # @allure.issue('https://baidu.com')
    # @allure.testcase('https://baidu.com')
    # @pytest.mark.flaky(reruns=3)
    # @pytest.mark.parametrize('case', case_data, ids=ids)
    @allure.description('综合用户登录')
    @pytest.mark.parametrize('case', case_data)
    def login_1(self, case):
        """综合用户登录"""
        self.log.info('demo, utl={}, data={}, header={}'.format(case['url'], case['data'], case['header']))
        if case['method'] == 'post_request_urlencoded':
            result = self.request.post_request_urlencoded(case['url'], case['data'], case['header'])
            self.log.info('响应结果：%s' % result)
            # 写入配置文件
            self.config.set_conf('parameter', 'token', result['data']['token'])
            self.config.set_conf('parameter', 'uuid', result['data']['uuid'])
            assert self.test.assert_text(result['code'], 1, case['test_name'])
            self.log.info('配置文件中token ={}'.format(self.config.get_conf('parameter', 'token')))
            self.log.info('配置文件中uuid ={}'.format(self.config.get_conf('parameter', 'uuid')))
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('客户端账号登录')
    @pytest.mark.parametrize('case', LoginK().case_data)
    def test_login_2(self, case):
        """客户端账号登录"""
        url = '%s%s' % ('http://', self.config.get_conf('test_host', 'test_order_url'))
        self.log.info("*************** 开始执行用例 ***************")
        self.log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url
                                        + case['url'], case['data'], case['header'], case['type'])
        self.log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        # 写入配置文件
        self.config.set_conf('APP', 'token', result['data']['token'])
        self.config.set_conf('APP', 'uuid', result['data']['uuid'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是：' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')