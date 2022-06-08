from common import read_yaml_data
import pytest
from common.class_requests import HttpSession
import json


# class Test_StandardPriceScheme:
#
#     parames_data = read_yaml_data.ReadYamlData2("Search_data2")
#
#     @pytest.mark.parametrize('method, url, json, expect, bool', parames_data)
#     def test_StandardPriceScheme(self, method, url, json, expect, bool, init1):
#         if not bool:
#             pytest.xfail(reason='测试用例不满足要求，暂时不执行！')
#         # data = json.loads(data)
#         # headers = json.loads(headers)
#         json = str(json)
#         try:
#             response = init1.request(method=method, url=url, json=eval(json))
#         except Exception as e:
#             print(e)
#         pass

#
# if __name__ == '__main__':
#     Test_StandardPriceScheme.test_StandardPriceScheme(init1=HttpSession())
#     pytest.main()