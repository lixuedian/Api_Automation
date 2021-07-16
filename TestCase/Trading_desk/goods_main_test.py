
import allure
import pytest

import TestCase
from Common import Consts
from Common.Methodes import notify, log
from Common.Mysql_operate import mysql_db
from Common.Parser import parser
from Params.params_goods import GetAllProductType, GetAllGoodsStatus, GetAllGoodsSort, GetGoodsListByCondition, \
    AddGoods, EditGoods, EnableLaunch, GetGoodsProductById, DeleteGoods

header = TestCase.Trading_desk.header('Trading')
BASE_PATH = TestCase.BASE_PATH
url = TestCase.Trading_desk.url


class TestGoods(object):

    @allure.description('获取产品类型下拉选项')
    @pytest.mark.parametrize('case', GetAllProductType().case_data)
    def test_goods_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取商品状态下拉选项')
    @pytest.mark.parametrize('case', GetAllGoodsStatus().case_data)
    def test_goods_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('获取商品排序集合')
    @pytest.mark.parametrize('case', GetAllGoodsSort().case_data)
    def test_goods_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('根据筛选条件分页获取商品列表')
    @pytest.mark.parametrize('case', GetGoodsListByCondition().case_data)
    def test_goods_04(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('新增商品')
    @pytest.mark.parametrize('case', AddGoods().case_data)
    def test_goods_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('修改商品')
    @pytest.mark.parametrize('case', EditGoods().case_data)
    def test_goods_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('上下架商品')
    @pytest.mark.parametrize('case', EnableLaunch().case_data)
    def test_goods_07(self, case):
        mysql = 'update test_mp_goods_center.goods_info set status = 3 where id = 68'
        mysql_db(mysql)
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('根据商品id查详情')
    @pytest.mark.parametrize('case', GetGoodsProductById().case_data)
    def test_goods_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('删除商品')
    @pytest.mark.parametrize('case', DeleteGoods().case_data)
    def test_goods_10(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
        log.info('响应结果：%s' % result)
        # parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH+'/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')


