from Params.params import get_parameter


class AddProject:
    """添加项目"""
    params = get_parameter('add_project')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetProjectListByCondition:
    """根据项目分类id和名称获取项目列表"""
    params = get_parameter('getProjectListByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddProjectType:
    """添加项目分类"""
    params = get_parameter('add_projectType')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetProjectTypes:
    """获取项目分类列表"""
    params = get_parameter('getProjectTypes')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetProjectTypeByName:
    """根据项目分类名称查询项目分类信息"""
    params = get_parameter('getProjectTypeByName')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddProperty:
    """新增动态属性"""
    params = get_parameter('add_property')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditProperty:
    """编辑动态属性"""
    params = get_parameter('edit_property')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetSearch:
    """查询动态属性"""
    params = get_parameter('get_Search')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOne:
    """获取一条动态属性的基本信息"""
    params = get_parameter('getOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class SearchModule:
    """搜索模块"""
    params = get_parameter('searchModule')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddPropertyField:
    """新增属性字段"""
    params = get_parameter('add_property_field')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditPropertyField:
    """修改属性字段"""
    params = get_parameter('edit_property_field')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPropertyField:
    """查询属性字段"""
    params = get_parameter('get_property_field')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOnePropertyField:
    """获取属性字段详情"""
    params = get_parameter('getOne_property_field')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
