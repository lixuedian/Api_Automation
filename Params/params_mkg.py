from Params.params import get_parameter


class FindById:
    """按项目分类ID查询项目列表"""
    params = get_parameter('findById')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class FindByProjectIdWithPage:
    """按项目ID查找商品列表"""
    params = get_parameter('findByProjectIdWithPage')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetInfoByGoodsId:
    """按商品ID获取商品信息"""
    params = get_parameter('getInfoByGoodsId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetLecturersByIdsAndCategoryId:
    """获取授课讲师信息"""
    params = get_parameter('getLecturersByIdsAndCategoryId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseContents:
    """按商品ID获取商品绑定的课程目录"""
    params = get_parameter('getCourseContents')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetUserInfo:
    """获取个人信息"""
    params = get_parameter('getUserInfo')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourses:
    """获取用户课程列表"""
    params = get_parameter('getCourses')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class TopCourse:
    """课程置顶"""
    params = get_parameter('topCourse')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CancelTopCourse:
    """课程取消置顶"""
    params = get_parameter('cancelTopCourse')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class MyGetCourseContents:
    """按课程ID获取课程目录"""
    params = get_parameter('my_getCourseContents')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPlayLink:
    """获取课程播放链接"""
    params = get_parameter('getPlayLink')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseHandouts:
    """按讲义ID获取讲义信息"""
    params = get_parameter('getCourseHandouts')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
