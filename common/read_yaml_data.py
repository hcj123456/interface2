import os

from string import Template

import yaml
from common.constant import YAML_DIR


def ReadYamlData(data, search):
    # path = os.path.dirname(os.path.dirname(__file__)) + os.sep + 'test_data' + os.sep + 'data.yml'
    path = os.path.join(YAML_DIR, 'data.yml')
    with open(path, encoding='utf-8') as f:
        f1 = f.read()
        f2 = Template(f1)  # 利用读取出来的数据生成Template对象
        f3 = f2.safe_substitute({'data': data})  # 使用Template对象调用safe_substitute({'yaml中变量值'：'新值'})方法修改yaml文件中指定的数据
    return yaml.safe_load(f3)[search]
    # obj = yaml.safe_load_all(f3)
    # for i in obj:
    #     print(i)


def ReadYamlData2(search):
    # path = os.path.dirname(os.path.dirname(__file__)) + os.sep + 'test_data' + os.sep + 'data.yml'
    path = os.path.join(YAML_DIR, 'data.yml')
    return yaml.safe_load(open(path, encoding='utf-8'))[search]