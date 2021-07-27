import allure
import pytest
from Common import Consts
from Common.Parser import parser
from Common.Methodes import notify, log
import TestCase
from Params.params_app100 import GetRoomLiveUrl, GetMyCourseList, MyLiveCourse,  ReturnMoneyShare, IndexOpen, \
    GradeList, OpenList, GetVieDeoWechat, CourseList, CouponNum, YuYue, SetPlayLog, UpdateToken, SetOrderTop, \
    SetDownLog, SetCourseDel, KeChengOpen, OfflineInfo, KenChengInfo, GoldBuy, GetSubject, \
    GetRoomEnterUrl, GetRecommend, GetRoll, GetMyCourseInfo, GetListOne, GetList2, GetList1, GetList0, GetCoupon, \
    GetExpDetail, CheckPay, GetCharge, TaskList, SetSchoolTime, MyOrder

header = TestCase.header_app
BASE_PATH = TestCase.BASE_PATH
url = TestCase.test_app100


class TestAPP100(object):
    @allure.description('（001）001-课程相关-获取直播间链接')
    @pytest.mark.parametrize('case', GetRoomLiveUrl().case_data)
    def test_app100_01(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（002）002-课程相关-获取我的课程列表')
    @pytest.mark.parametrize('case', GetMyCourseList().case_data)
    def test_app100_02(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（004）004-课程相关-练习首页正在直播公开课和我的直播课程')
    @pytest.mark.parametrize('case', MyLiveCourse().case_data)
    def test_app100_03(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（006）006-课程相关-获取推荐返现分享信息')
    @pytest.mark.parametrize('case', ReturnMoneyShare().case_data)
    def test_app100_05(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（007）007-课程相关-首页最新公共课')
    @pytest.mark.parametrize('case', IndexOpen().case_data)
    def test_app100_06(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（008）008-课程相关-班级列表')
    @pytest.mark.parametrize('case', GradeList().case_data)
    def test_app100_07(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（009）009-课程相关-公开课')
    @pytest.mark.parametrize('case', OpenList().case_data)
    def test_app100_08(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（010）010-课程相关-视频播放页面，班主任微信接口')
    @pytest.mark.parametrize('case', GetVieDeoWechat().case_data)
    def test_app100_09(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（011）011-课程相关-推荐课程（首页）')
    @pytest.mark.parametrize('case', CourseList().case_data)
    def test_app100_10(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（0012）012-课程相关-优惠券数量')
    @pytest.mark.parametrize('case', CouponNum().case_data)
    def test_app100_11(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（013）013-课程相关-课程预约')
    @pytest.mark.parametrize('case', YuYue().case_data)
    def test_app100_12(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（015）015-课程相关-播放记录')
    @pytest.mark.parametrize('case', SetPlayLog().case_data)
    def test_app100_13(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（014）014-课程相关-我的课程-取得新的token')
    @pytest.mark.parametrize('case', UpdateToken().case_data)
    def test_app100_14(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（016）016-课程相关-课程置顶-删除/恢复')
    @pytest.mark.parametrize('case', SetOrderTop().case_data)
    def test_app100_15(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（018）018-课程相关-下载次数记录')
    @pytest.mark.parametrize('case', SetDownLog().case_data)
    def test_app100_16(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（019）019-课程相关-订单删除/恢复')
    @pytest.mark.parametrize('case', SetCourseDel().case_data)
    def test_app100_17(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（020）020-课程相关-所有公共课')
    @pytest.mark.parametrize('case', KeChengOpen().case_data)
    def test_app100_18(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（021）021-课程相关-购买线下-信息完善')
    @pytest.mark.parametrize('case', OfflineInfo().case_data)
    def test_app100_19(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（022）022-课程相关-班级课程详情')
    @pytest.mark.parametrize('case', KenChengInfo().case_data)
    def test_app100_20(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（023）023-课程相关-金币购买课程')
    @pytest.mark.parametrize('case', GoldBuy().case_data)
    def test_app100_21(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（024）024-课程相关-获取学')
    @pytest.mark.parametrize('case', GetSubject().case_data)
    def test_app100_22(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（025）025-课程相关-进入教室')
    @pytest.mark.parametrize('case', GetRoomEnterUrl().case_data)
    def test_app100_23(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（027）027-课程相关-视频播放-课程推荐')
    @pytest.mark.parametrize('case', GetRecommend().case_data)
    def test_app100_25(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（026）026-课程相关-获取滚动数据')
    @pytest.mark.parametrize('case', GetRoll().case_data)
    def test_app100_26(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（028）028-课程相关-课程-视频列表')
    @pytest.mark.parametrize('case', GetMyCourseInfo().case_data)
    def test_app100_27(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（029）029-课程相关-班级列表')
    @pytest.mark.parametrize('case', GetListOne().case_data)
    def test_app100_28(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（030）030-课程相关-课程目录')
    @pytest.mark.parametrize('case', GetList2().case_data)
    def test_app100_29(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（031）031-课程相关-课程列表-新版')
    @pytest.mark.parametrize('case', GetList1().case_data)
    def test_app100_30(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（032）032-课程相关-课程列表-新版1.7.0（推荐到首页）')
    @pytest.mark.parametrize('case', GetList0().case_data)
    def test_app100_31(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（033）033-课程相关-获取优惠券数据')
    @pytest.mark.parametrize('case', GetCoupon().case_data)
    def test_app100_32(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（034）034-课程相关-获取物流详情')
    @pytest.mark.parametrize('case', GetExpDetail().case_data)
    def test_app100_33(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（035）035-课程相关-是否已经支付')
    @pytest.mark.parametrize('case', CheckPay().case_data)
    def test_app100_34(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（036）036-课程相关-ping++取得charge对象')
    @pytest.mark.parametrize('case', GetCharge().case_data)
    def test_app100_35(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（037）037-课程相关-任务中心')
    @pytest.mark.parametrize('case', TaskList().case_data)
    def test_app100_36(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（040）003-用户相关-设置学校、毕业时间')
    @pytest.mark.parametrize('case', SetSchoolTime().case_data)
    def test_app100_37(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')

    @allure.description('（041）004-用户相关-我的订单')
    @pytest.mark.parametrize('case', MyOrder().case_data)
    def test_app100_38(self, case):
        log.info("*************** 开始执行用例 ***************")
        log.info("用例名称  ==>> {}".format(case['test_name']))
        for i in range(1, 2):
            result = notify().notify_result(case['mode'], url + case['url'], case['data'], header, case['type'])
            log.info('响应结果：%s' % result)
            parser(result, case['test_name'], case['parser'], case['expected'])
        allure.attach.file(BASE_PATH + '/Log/log.log', '附件内容是： ' + '调试日志', '我是附件名', allure.attachment_type.TEXT)
        Consts.RESULT_LIST.append('True')
