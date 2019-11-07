"""
工具类
"""


class User:
    """账号信息"""

    def __init__(self, name, pwd):
        """初始化"""
        self.name = name
        self.pwd = pwd

    def valid(self):
        """是否验证通过"""
        print(self.name + ' 验证通过')


#  创建实例
user = User('zhangjian', '1992')
print('账号名：' + user.name)
print('密码：' + user.pwd)
# 调用实例方法
user.valid()
