from Config.Config import Config
from Common import Assert


test = Assert.Assertions()

config = Config()
url = config.test_url
url = '%s%s' % ('http://', url)

test_mp_url = '%s%s' % ('http://', config.get_conf('Trading', 'c_url'))


def header(TEXT):
    token = config.get_conf(TEXT, 'token')
    uuid = config.get_conf(TEXT, 'uuid')
    header = {
        'Content-Type': 'application/json',
        'token': token,
        'userid': uuid,
        'projectid': '110'
    }
    return header
