import allure
import pytest
from Common import Consts
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_mkg import FindByProjectIdWithPage, GetInfoByGoodsId, GetLecturersByIdsAndCategoryId, \
    GetCourseContents, GetUserInfo, GetCourses, TopCourse, CancelTopCourse, MyGetCourseContents, GetPlayLink, \
    GetCourseHandouts, FindById
from Params.params_order import OrderPrePurchase, CreateOrder, GetPayment, RepayOrder, CancelOrders, GetDetailByOrderId, \
    GetOrders, CreateOrder1

header = TestCase.TradingDesk.mkg_header
BASE_PATH = TestCase.BASE_PATH
url = TestCase.TradingDesk.test_mkg_url


class TestCreateOrder(object):
    @allure.description('创建订单')
    @pytest.mark.parametrize('case', CreateOrder1().case_data)
    def test_create_order_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


class TestMkg(object):
    @allure.description('商品确认页面')
    @pytest.mark.parametrize('case', OrderPrePurchase().case_data)
    def test_mkg_order_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('创建商品订单+支付')
    @pytest.mark.parametrize('case', CreateOrder().case_data)
    def test_mkg_order_02(self, case):
        orderId = ''
        orderNo = ''
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
            orderId = result['data']['orderId']
            orderNo = result['data']['orderNo']
            paymentLink = result['data']['paymentLink']
            log.info("打印支付链接：%s" % paymentLink)

        log.info("*************** 开始执行用例 ***************")
        """查询订单详情"""
        case = GetDetailByOrderId().case_data
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        data = {
            'orderId': orderId,
            'orderNo': orderNo
        }
        for i in range(1, 2):
            result = notify().notify_result(case[0]['mode'], url + case[0]['url'], data, header, case[0]['type'])
            log.info('响应结果：%s' % result)
            parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

        log.info("*************** 开始执行用例 ***************")
        """获取支付信息"""
        case = GetPayment().case_data
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        data = {
            'orderId': orderId,
            'orderNo': orderNo
        }
        for i in range(1, 2):
            result = notify().notify_result(case[0]['mode'], url + case[0]['url'], data, header, case[0]['type'])
            log.info('响应结果：%s' % result)
            parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])

        log.info("*************** 开始执行用例 ***************")
        """订单重新支付"""
        case = RepayOrder().case_data
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        data = {
            'orderId': orderId,
            'orderNo': orderNo,
            'paymentMethod': 10,
            'projectCategoryId': 1
        }
        for i in range(1, 2):
            result = notify().notify_result(case[0]['mode'], url + case[0]['url'], data, header, case[0]['type'])
            log.info('响应结果：%s' % result)
            parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])
            paymentLink = result['data']['paymentLink']
            log.info("打印支付链接：%s" % paymentLink)

        log.info("*************** 开始执行用例 ***************")
        """取消订单"""
        case = CancelOrders().case_data
        log.info("用例名称  ==>> {}".format(case[0]['test_name']))
        data = {
            'orderId': orderId,
            'orderNo': orderNo,
            'paymentMethod': 10
        }
        for i in range(1, 2):
            result = notify().notify_result(case[0]['mode'], url + case[0]['url'], data, header, case[0]['type'])
            log.info('响应结果：%s' % result)
            parser(result, case[0]['test_name'], case[0]['parser'], case[0]['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取订单列表')
    @pytest.mark.parametrize('case', GetOrders().case_data)
    def test_mkg_order_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按项目分类ID查询项目列表')
    @pytest.mark.parametrize('case', FindById().case_data)
    def test_mkg__04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按项目ID查找商品列表')
    @pytest.mark.parametrize('case', FindByProjectIdWithPage().case_data)
    def test_mkg_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按商品ID获取商品信息')
    @pytest.mark.parametrize('case', GetInfoByGoodsId().case_data)
    def test_mkg_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取授课讲师信息')
    @pytest.mark.parametrize('case', GetLecturersByIdsAndCategoryId().case_data)
    def test_mkg_07(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按商品ID获取商品绑定的课程目录')
    @pytest.mark.parametrize('case', GetCourseContents().case_data)
    def test_mkg_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取个人信息')
    @pytest.mark.parametrize('case', GetUserInfo().case_data)
    def test_mkg_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取用户课程列表')
    @pytest.mark.parametrize('case', GetCourses().case_data)
    def test_mkg_10(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('课程置顶')
    @pytest.mark.parametrize('case', TopCourse().case_data)
    def test_mkg_11(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('课程取消置顶')
    @pytest.mark.parametrize('case', CancelTopCourse().case_data)
    def test_mkg_12(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按课程ID获取课程目录')
    @pytest.mark.parametrize('case', MyGetCourseContents().case_data)
    def test_mkg_13(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取课程播放链接')
    @pytest.mark.parametrize('case', GetPlayLink().case_data)
    def test_mkg_14(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('按讲义ID获取讲义信息')
    @pytest.mark.parametrize('case', GetCourseHandouts().case_data)
    def test_mkg_15(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
