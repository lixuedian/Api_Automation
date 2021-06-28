# _*_ coding : UTF-8
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/18 8:22
# 文件名称 ： Methodes.py
# 开发工具 ： PyCharm

from Common import Request, GToken as Gt
from Config.Config import Config
from Common import Log
import json as complexions

request = Request.Request()
config = Config()
log = Log.MyLog()


class notify(object):
    def token(self):
        if Gt.get_token() == None:
            token = config.get_conf('parameter', 'token')
        else:
            token = Gt.get_token()
        return token

    def notify_result(self, mode, url, data, header, f_type):
        self.request_log(url, mode, data, header)
        # 请求方式
        numbers = {
            0: self.get_request,
            1: self.post_request,
            2: self.post_request_multipart,
            3: self.post_request_urlencoded,
            4: self.put_request

        }
        method = numbers.get(mode)
        if mode == 1:
            if method:
                res = method(url, data, header, f_type)
            return res
        elif mode in (0, 2, 3, 4):
            if method:
                res = method(url, data, header)
            return res
        else:
            assert AssertionError

    def get_request(self, url, data, header):
        """
        获取枪头详情信息
        :param url:
        :param data:
        :param header:
        :return:
        """
        # header['token'] = self.token()
        result = request.get_request(url, data, header)
        return result

    def post_request(self, url, data, header, f_type):
        """
        根据用户，枪头编号查询可用账户
        :param f_type:
        :param url:
        :param data:
        :param header:
        :return:
        """
        # header['token'] = self.token()
        result = request.post_request(url, data, header, f_type)
        return result

    def post_request_multipart(self, url, data, header):
        """
        获取幂等型接口调用所需的token
        :param url:
        :param data:
        :param header:
        :return:
        """
        header['token'] = self.token()
        result = request.post_request_multipart(url, data, header, 'file_parm', 'file', 'f_type')
        return result

    def post_request_urlencoded(self, url, data, header):
        header['token'] = self.token()
        result = request.post_request_urlencoded(url, data, header)
        return result

    def put_request(self, url, data, header):
        header['token'] = self.token()
        result = request.post_request_urlencoded(url, data, header)
        return result

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        log.info("接口请求地址 ==>> {}".format(url))
        log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        # log.info("接口请求头 ==>> {}".format(complexions.dumps(headers, indent=4, ensure_ascii=False)))
        # log.info("接口请求 params 参数 ==>> {}".format(complexions.dumps(params, indent=4, ensure_ascii=False)))
        log.info("接口参数 ==>> {}".format(complexions.dumps(data, indent=4, ensure_ascii=False)))
        # log.info("接口请求体 json 参数 ==>> {}".format(complexions.dumps(json, indent=4, ensure_ascii=False)))
        # log.info("接口上传附件 files 参数 ==>> {}".format(files))
        # log.info("接口 cookies 参数 ==>> {}".format(complexions.dumps(cookies, indent=4, ensure_ascii=False)))
