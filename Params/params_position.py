"""
定义所有测试数据

"""
import os
from Common import Log
from Params.params import get_parameter
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class Banner:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('banner')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Region:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RegionCity:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region_city')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RegionCityRegion:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('region_city_region')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Collect:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('collect')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Cancel:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('cancel')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CollectList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('CollectList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionDetail:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_detail')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionFind:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_find')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionDataList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_dataList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionYearList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_yearList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PositionQueryList:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Position.yaml')
    params = get_parameter('position_query_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
