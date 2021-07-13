from Params.params import get_parameter


class AddGoods:
    """新增商品"""
    params = get_parameter('goods_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteGoods:
    """删除商品"""
    params = get_parameter('goods_delete')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditGoods:
    """编辑商品"""
    params = get_parameter('goods_edit')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAllProductType:
    """获取产品类型"""
    params = get_parameter('getAllProductType')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAllGoodsStatus:
    """获取商品状态"""
    params = get_parameter('getAllGoodsStatus')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAllGoodsSort:
    """获取商品排序集合"""
    params = get_parameter('getAllGoodsSort')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetGoodsListByCondition:
    """根据筛选条件分页获取商品列表"""
    params = get_parameter('getGoodsListByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EnableLaunch:
    """上下架商品"""
    params = get_parameter('enableLaunch')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class LaunchGoodsByTimer:
    """定时上架商品"""
    params = get_parameter('launchGoodsByTimer')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetGoodsProductById:
    """根据商品id查详情"""
    params = get_parameter('getGoodsProductById')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
