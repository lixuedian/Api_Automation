from Params.params import get_parameter


class AddGoods:
    """添加一个课程"""
    params = get_parameter('goods_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteGoods:
    """添加一个课程"""
    params = get_parameter('goods_delete')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditGoods:
    """编辑课程"""
    params = get_parameter('goods_edit')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OpenOrCloseGoods:
    """启用/禁用课程"""
    params = get_parameter('goods_openOrClose')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOneCourse:
    """获取一个课程的详细信息(基本字段和动态字段)"""
    params = get_parameter('getOneCourse')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseList:
    """分页获取课程列表"""
    params = get_parameter('GetCourseList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddProject:
    """添加项目"""
    params = get_parameter('project_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
