# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： params.py
# 开发工具 ： PyCharm
"""
定义所有测试数据

"""
import os
from Params import tools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    log.info('读取配置参数中请稍等')
    print('读取配置参数中请稍等')
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Process:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Process.yaml')
    params = get_parameter('Process')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
        # print(params)


