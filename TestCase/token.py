import TestCase.Trading_desk
import requests
from Params.params import ZTLogin
from Config.Config import Config


def zt_token():
    url = TestCase.Trading_desk.url
    case = ZTLogin().case_data
    result = requests.get(url=url + case[0]['url'], params=case[0]['data'], headers=case[0]['header'])
    result = result.json()
    token = result['data']['token']
    uuid = str(result['data']['id'])
    Config().write_configuration('Trading', token, uuid)




