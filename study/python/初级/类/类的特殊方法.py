# __dict__  获得类对象或实例对象所绑定的所有属性和方法的字典
# __len__()  通过重写_len___()方法，让内置函数len()的参数可以是自定义类型
# __add__)  通过重写_add__()方法，可使用自定义对象具有“+”功能
# __new_()  用于创建对象
# __init___()  对创建的对象进行初始化

class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2
print(s)

print(stu1.__len__())
