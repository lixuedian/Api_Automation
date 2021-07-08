from Params.params import get_parameter


class AddHandout:
    """新增讲义"""
    params = get_parameter('add_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditHandout:
    """编辑讲义"""
    params = get_parameter('edit_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OpenOrCloseBranch:
    """批量启用禁用讲义"""
    params = get_parameter('openOrCloseBranch_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteBranch:
    """批量删除讲义"""
    params = get_parameter('deleteBranch_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetListByProjectId:
    """根据项目id查询讲义列表(项目id在请求头中)"""
    params = get_parameter('getListByProjectId_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetListByCondition:
    """根据项目id和筛选条件查询讲义列表"""
    params = get_parameter('getListByCondition_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetHandoutListItem:
    """根据讲义id搜索讲义列表项信息"""
    params = get_parameter('getHandoutListItem_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetHandoutBaseInfo:
    """根据讲义id搜索讲义基本信息"""
    params = get_parameter('getHandoutBaseInfo_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetHandOutTypeEnum:
    """讲义类型枚举"""
    params = get_parameter('getHandOutTypeEnum_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOrderByEnum:
    """排序类型枚举"""
    params = get_parameter('getOrderByEnum_handout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])

