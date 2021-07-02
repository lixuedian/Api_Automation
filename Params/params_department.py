from Params.params import get_parameter


class DepartmentList:
    """获取部门的树状结构"""
    params = get_parameter('department_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DepartmentUpdate:
    """更新部门备注"""
    params = get_parameter('department_update')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DepartmentUser:
    """查询该部门下的员工,分页"""
    params = get_parameter('departmentUser')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetUser:
    """通过各种查询条件查询用户，单条"""
    params = get_parameter('getUser')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Update:
    """通过各种查询条件查询用户，单条"""
    params = get_parameter('update')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetUserList:
    """多条件组合查询该部门下员工，多条"""
    params = get_parameter('getUserList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class IsBussinessInUse:
    """判断某条业务线是否在用"""
    params = get_parameter('isBussinessInUse')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class ResetPassword:
    """管理员重置密码"""
    params = get_parameter('password_reset')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class ChangePassword:
    """用户修改密码"""
    params = get_parameter('password_change')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])