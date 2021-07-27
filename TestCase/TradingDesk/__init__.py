from Config.Config import Config

config = Config()
url = config.test_url
url = '%s%s' % ('http://', url)

test_mp_url = '%s%s' % ('http://', config.get_conf('Trading', 'c_url'))
test_mkg_url = '%s%s' % ('http://', config.get_conf('Trading', 'm_url'))
mkg_header = config.header_json('mkg')
zt_header = config.header_json('Trading')


# def header(TEXT):
#     token = config.get_conf(TEXT, 'token')
#     uuid = config.get_conf(TEXT, 'uuid')
#     headers = {
#         'Content-Type': 'application/json',
#         'token': token,
#         'userid': uuid,
#         'projectid': '110'
#     }
#     return headers

