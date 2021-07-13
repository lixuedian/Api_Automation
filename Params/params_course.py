from Params.params import get_parameter


class GetCourseType:
    """获取课程类型"""
    params = get_parameter('getCourseType')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CourseList:
    """分页获取课程列表"""
    params = get_parameter('course_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CourseDelete:
    """删除课程"""
    params = get_parameter('course_delete')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CourseOpenOrClose:
    """启用禁用课程"""
    params = get_parameter('course_openOrClose')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetDynamicFieldList:
    """获取动态字段"""
    params = get_parameter('getDynamicFieldList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeachType:
    """获取授课形式"""
    params = get_parameter('getTeachType')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetRegion:
    """获取地区"""
    params = get_parameter('getRegion')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CourseAdd:
    """添加课程"""
    params = get_parameter('course_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CourseEdit:
    """编辑课程"""
    params = get_parameter('course_edit')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseBaseInfo:
    """获取课程的基本信息"""
    params = get_parameter('getCourseBaseInfo')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
