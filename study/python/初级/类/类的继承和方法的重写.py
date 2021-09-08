class Person(object):  # Person类继承object类
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_nmb):
        super().__init__(name, age)
        self.stu_nmb = stu_nmb
    # ---------------方法的重写---------重写父类方法----------------------
    def info(self):
        super().info()
        print(self.stu_nmb)


class Teacher(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    def info(self):
        super().info()
        print(self.year)

stu = Student('张三', 20, 1011)
tec = Teacher('李四', 30, 5)
stu.info()
tec.info()


# 想继承2个类 就在括号内多写一个想继承的类的名字
class set(Student, Teacher):
    pass
