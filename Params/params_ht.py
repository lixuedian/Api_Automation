from Params.params import get_parameter


class Logout:
    """登出"""
    params = get_parameter('Logout')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Permission:
    """获取用户具体权限"""
    params = get_parameter('permission')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Sso:
    """sso接口，判断用户是否已登陆"""
    params = get_parameter('sso')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RoleLIst:
    """根据部门获取已绑定相关角色"""
    params = get_parameter('role_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetUsableRole:
    """根据部门获取已绑定相关角色"""
    params = get_parameter('getUsableRole')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RoleAdd:
    """添加角色"""
    params = get_parameter('role_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OauthList:
    """获取角色信息"""
    params = get_parameter('oauth_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOauth:
    """根据id获取角色信息"""
    params = get_parameter('get_oauth')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditOauth:
    """根据id编辑角色信息"""
    params = get_parameter('edit_oauth')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteOauth:
    """根据id编辑角色信息"""
    params = get_parameter('delete_oauth')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddDepartment:
    """给部门添加角色"""
    params = get_parameter('department_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DelRoleDepartment:
    """从部门下删除角色"""
    params = get_parameter('department_delRole')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])