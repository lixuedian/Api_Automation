from Params.params import get_parameter


class Login:
    # log.info('解析yaml, Path:' + path_dir + '/Params/Param/Login.yaml')
    params = get_parameter('Login')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class ZTLogin:
    params = get_parameter('ZT_login')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
