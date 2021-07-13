from Params.params import get_parameter


class AddAudio:
    """新增音频"""
    params = get_parameter('addAudio')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddVideo:
    """新增视频"""
    params = get_parameter('addVideo')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditVideo:
    """编辑音视频"""
    params = get_parameter('edit_Video')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAudioBaseInfo:
    """根据id搜索音视频基本信息"""
    params = get_parameter('getAudioBaseInfo')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOneAudioListInfo:
    """根据id搜索音视频列表信息"""
    params = get_parameter('getOneAudioListInfo')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAudioListByProjectId:
    """根据项目id获取音频列表"""
    params = get_parameter('getAudioListByProjectId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetVideoListByProjectId:
    """根据项目id获取视频列表"""
    params = get_parameter('getVideoListByProjectId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetVideoBaseInfoById:
    """根据音视频id获取音视频的基本信息"""
    params = get_parameter('getVideoBaseInfoById')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteVideoBranch:
    """批量删除音视频"""
    params = get_parameter('deleteVideoBranch')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OpenOrCloseBranch:
    """批量启用禁用音视频"""
    params = get_parameter('openOrCloseBranch')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAudioListByCondition:
    """根据筛选条件获取音频列表"""
    params = get_parameter('getAudioListByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetVideoListByCondition:
    """根据筛选条件获取视频列表"""
    params = get_parameter('getVideoListByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])

