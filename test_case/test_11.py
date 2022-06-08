# import pytest
#
# import re
# @pytest.fixture(scope='function', autouse=True)
# @pytest.fixture(scope='function', params=[], autouse=True)
# def function1(request):
#     user = request.param
#     print('慢慢{}'.format(user))
#     yield user
#     print('门口慢慢来')
#
#
# # @pytest.mark.usefixtures('function1')
# class Test_22:
#     # @pytest.mark.usefixtures('function1')   #不需要使用fixture中得返回值，则直接使用这个@pytest.mark.usefixtures调用
#     @pytest.mark.parametrize('function1', ['11', '22', '33'], indirect=True)
#     def test_function2(self, function1):    #需要使用fixture中得返回值，则在方法中直接调用
#         print('用例中的数值{}'.format(function1))


# p = 'e,r,r'
# t = p.split('-')
# print(t)

# p = 'kkk'
# o = '123'
# tt = p + o
# print(type(tt))
# tr={"m":2, "popo": "njnj"}
# ty={"m":2, "mk":67}
# tr.update(ty)
# print(tr)
# list=[]
# print(tr.items())
# for i,t in tr.items():
#     list.append(i)
#     list.append(t)
# print(list)
# li=[1,2,33,44,33,1,2,5,66]
# set1=set(li)    #----去重后为字典格式
# print(set1)
# li=list(set1)
# print(li)
li=['huh','koko','hugg','drrv']
print(list(enumerate(li)))
print(list(enumerate(li,3)))
for index,i in enumerate(li,3):
    print(index,i)
