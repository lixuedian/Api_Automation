# 短信管理
from Params.params import get_parameter


class GetMassSmsTaskList:
    """获取短信任务列表"""
    params = get_parameter('getMassSmsTaskList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddMassSmsTaskOne:
    """添加短信任务"""
    params = get_parameter('addMassSmsTaskOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetNonuseUserList:
    """获取免扰用户列表"""
    params = get_parameter('getNonuseUserList')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DelNonuseUserOne:
    """删除单条免扰用户"""
    params = get_parameter('delNonuseUserOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
