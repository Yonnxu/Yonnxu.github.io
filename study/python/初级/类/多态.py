class Animal:
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('吃骨头')


class Cat(Animal):
    def eat(self):
        print('吃鱼')


class Person:
    def eat(self):
        print('五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
