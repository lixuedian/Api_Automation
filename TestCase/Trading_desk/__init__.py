from Config.Config import Config
from Common import Assert


test = Assert.Assertions()

config = Config()
url = config.test_url
url = '%s%s' % ('http://', url)


def header():
    token = config.get_conf('Trading', 'token')
    uuid = config.get_conf('Trading', 'uuid')
    header = {
        'Content-Type': 'application/json',
        'token': token,
        'userid': uuid,
        'projectid': '110'
    }
    return header
