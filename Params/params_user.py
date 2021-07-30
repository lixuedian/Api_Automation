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


class GetVerifyCode:
    """sso接口，判断用户是否已登陆"""
    params = get_parameter('getVerifyCode')
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


class PermissionDisplay:
    """资源列表展示状态调整入口"""
    params = get_parameter('permission_display')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PermissionDelete:
    """资源信息删除"""
    params = get_parameter('permission_delete')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PermissionGet:
    """获取资源信息byId"""
    params = get_parameter('permission_get')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PermissionEdit:
    """根据id修改资源信息"""
    params = get_parameter('permission_edit')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class MenuAdd:
    """添加菜单权限"""
    params = get_parameter('menu_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class MenuList:
    """菜单列表"""
    params = get_parameter('menu_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class FuncAdd:
    """添加功能权限"""
    params = get_parameter('func_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class FuncList:
    """功能列表"""
    params = get_parameter('func_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPermissionsByLevel:
    """指定获取几级菜单"""
    params = get_parameter('getPermissionsByLevel')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserRoleAdd:
    """给用户添加自定义角色"""
    params = get_parameter('user_role_add')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserRoleDelete:
    """删除用户自定义角色"""
    params = get_parameter('user_role_delete')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserRoleList:
    """获取用户角色列表"""
    params = get_parameter('user_role_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserGetUsableRole:
    """获取用户可用角色列表"""
    params = get_parameter('user_getUsableRole')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Status:
    """禁用、启用用户角色"""
    params = get_parameter('status')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPermissionByRole:
    """根据角色获取对应的权限信息"""
    params = get_parameter('getPermissionByRole')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PrDelePermissionByRole:
    """根据角色修改对应的权限信息"""
    params = get_parameter('DelePermissionByRole')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class SmsCode:
    """c端验证码发送接口"""
    params = get_parameter('smsCode')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserSso:
    """c端鉴权接口"""
    params = get_parameter('user_sso')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class UserCaptcha:
    """c端图形验证码"""
    params = get_parameter('user_captcha')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeacherByProjectCategoryId:
    """获取现后台该业务线下所有的老师列表"""
    params = get_parameter('getTeacherByProjectCategoryId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeacherByIdAndCategoryId:
    """获取该业务线下的老师"""
    params = get_parameter('getTeacherByIdAndCategoryId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeacherByMobileAndCategoryId:
    """通过手机号获取该业务线下的老师"""
    params = get_parameter('getTeacherByMobileAndCategoryId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
