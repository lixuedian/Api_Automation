from Params.params import get_parameter


class CatOne:
    """001-题库-app首页 题库分类一级"""
    params = get_parameter('catOne')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class AddAnswer:
    """002-题库-app首页-提交答案"""
    params = get_parameter('addAnswer')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CatLists:
    """003-题库-app首页 题库分类"""
    params = get_parameter('catLists')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetQuestion:
    """004-题库-app首页 抽题接口"""
    params = get_parameter('getQuestion')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class ClearHistory:
    """004-题库-清空答题记录"""
    params = get_parameter('clearHistory')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
