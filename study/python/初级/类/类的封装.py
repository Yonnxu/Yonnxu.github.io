class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车启动')


# 类的外部使用
car = Car('wryyyy')
car.start()
print(car.brand)


# 如果不希望类里面的属性被调用 则在前面加2个下划线 __
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()

print(stu.name)
# print(stu.__age) 无法调用
print(dir(stu))
# 如果真要使用需要_Student__age访问
print(stu._Student__age)