
import allure
import pytest
from Common.Methodes import notify
from Config.Config import Config
from Params.params_express import *
from Common import Log
from Common import Consts
from Common.Parser import parser
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config = Config()
notify = notify()
log = Log.MyLog()
url = config.test_express_url
url = '%s%s' % ('https://', url)


class TestExpress(object):
    data = GetExpressList()
    case_data = data.case_data

    @allure.description('获取订单物流列表')
    @pytest.mark.parametrize('case', case_data)
    def test_express_01(self, case):
        TestExpress.test_express_01.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')

    data = GetExpressTracesOne()
    case_data = data.case_data

    @allure.description('获取物流进度')
    @pytest.mark.parametrize('case', case_data)
    def test_express_02(self, case):
        TestExpress.test_express_02.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')

    data = SetExpressOne()
    case_data = data.case_data

    @allure.description('修改物流订单收件信息')
    @pytest.mark.parametrize('case', case_data)
    def test_express_03(self, case):
        TestExpress.test_express_03.__doc__ = case['test_name']
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        # 判断请求方法
        result = notify.notify_result(case['mode'], url+case['url'], case['data'], case['header'], case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        log.info("*************** 结束执行用例 ***************")
        Consts.RESULT_LIST.append('True')
