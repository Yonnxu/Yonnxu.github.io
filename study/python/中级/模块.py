# 模块当中可以包含多个 函数 类和语句


def fun():
    pass
def fun2():
    pass
class Student:
    native_place:'吉林'
    def eat(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass

a=10
b=20
print(a+b)