import yaml
import os


def read_testcase_yaml(yaml_name):
    with open(os.getcwd()+"/Params/Param/" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 清除yaml文件
def write_extract_yaml(data):
    with open(os.getcwd()+"/extract.yml", mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清除yaml文件
def clear_extract_yaml():
    with open(os.getcwd()+"/extract.yml", mode='w', encoding='utf-8') as f:
        f.truncate()


class YamlUtil(object):
    pass
