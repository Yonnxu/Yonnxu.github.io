class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 1.变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 2.类的浅拷贝
print('--------------------')
disk = Disk()  # 创建一个硬盘类的对象
computer = Computer(cpu1, disk)  # 创建一个计算机类的对象

# 浅拷贝
import copy

computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# 深拷贝
print('--------------------')
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
# ----------------------------------个人理解-----------------------------
# 只是赋值：把拷贝对象的id 还有值的地址都复制一遍 如果拷贝对象对原数据进行了修改 则拷贝的那份也会随之改变
# 浅拷贝：把拷贝对象的id地址改变 但是值的id地址不变 也就是如果原对象被修改 拷贝的那份不会被修改 但是如果把下面的值修改 则拷贝和原份的值都改变
# 深拷贝：带上值一起拷贝 无论原来地址的值如何变化 拷贝的那份值都不变
