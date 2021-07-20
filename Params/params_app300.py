from Params.params import get_parameter


class IndexMoKao:
    """模考相关V1版本-获取首页模考"""
    params = get_parameter('indexMokao')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class MoZhenTi:
    """模考相关V1版本-获取首页模考-真题"""
    params = get_parameter('MoZhenTi')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Subscribe:
    """模考相关V1版本-预约模考"""
    params = get_parameter('subscribe')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RankingNew:
    """模考相关V1版本-模考大赛详情"""
    params = get_parameter('rankingNew')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RankingList:
    """模考相关V1版本-模考排行榜"""
    params = get_parameter('rankingList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetZhenTiDataNew:
    """模考相关V1版本-获取真题数据"""
    params = get_parameter('getZhenTiDataNew')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetZhenTiCat:
    """真题相关V1版本-app首页-阶段类型-能力分类（用于切换）"""
    params = get_parameter('getZhenTiCat')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class ZhenTi:
    """模考相关V1版本-真题列表"""
    params = get_parameter('ZhenTi')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetZhenTiData:
    """模考相关V1版本-获取真题题目数据"""
    params = get_parameter('getZhenTiData')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
