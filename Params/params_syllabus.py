from Params.params import get_parameter


class GetSyllabus:
    """课程大纲查询"""
    params = get_parameter('findByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class DeleteSyllabus:
    """删除章节课次"""
    params = get_parameter('delete_syllabus')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeachTypeS:
    """授课形式"""
    params = get_parameter('getTeachType_s')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTeacher:
    """上课老师"""
    params = get_parameter('getTeacher')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseTimesStatus:
    """课次状态"""
    params = get_parameter('getCourseTimesStatus')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddChapter:
    """添加章节"""
    params = get_parameter('addChapter')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetChapterById:
    """根据章节id获取章节信息"""
    params = get_parameter('getChapterById')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditChapter:
    """修改章节信息"""
    params = get_parameter('editChapter')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetAllChapter:
    """获取所有章"""
    params = get_parameter('getAllChapter')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetCourseTimesById:
    """根据课次id查询课次信息接口"""
    params = get_parameter('getCourseTimesById')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddCourseTimes:
    """增加课次"""
    params = get_parameter('addCourseTimes')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class EditCourseTimes:
    """编辑课次"""
    params = get_parameter('editCourseTimes')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetTreeChapters:
    """获取章节（树形结构）"""
    params = get_parameter('getTreeChapters')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class FindByCondition:
    """模糊查询讲义视频音频"""
    params = get_parameter('findByCondition')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
