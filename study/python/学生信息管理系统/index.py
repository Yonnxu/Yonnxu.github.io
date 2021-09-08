import os

filename = 'student.txt'


def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确认要退出系统？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menm():
    print('学生信息管理系统'.center(60, '='))
    print('功能菜单'.center(60, '-'))
    print('1.录入学生信息'.rjust(15), ' ')
    print('2.查找学生信息'.rjust(15), ' ')
    print('3.删除学生信息'.rjust(15), ' ')
    print('4.修改学生信息'.rjust(15), ' ')
    print('5.排序'.rjust(11), ' ')
    print('6.统计学生总人数'.rjust(16), ' ')
    print('7.显示所有学生信息'.rjust(17), ' ')
    print('0.退出'.rjust(11), ' ')
    print(''.center(60, '='))


def insert():
    student_list = []
    while True:
        id = input('请输入id(如:1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            java = int(input('请输入Java成绩: '))
        except:
            print('输入无效,请重新输入')
            continue
        # 把录入的信息保存到字典
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 把学生信息添加到列表
        student_list.append(student)
        answer = input('是否继续添加?y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('录入完毕')


# 保存到文件当中
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


# 查询
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按id查找请输入1，按姓名查找请输入2: ')
            if mode == '1':
                id = input('请输入学生id')
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print('输入错误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))  # 字符串转化为字典类型
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    if name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)  # 清空列表
            student_query.clear()
            answer = input('是否要继续查询?y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查到信息')
        return

    # 定义标题显示格式
    format_title = '{:^6}\t{:^12]\t{:^8}it{:^10}\t{:^10}\t{:^8}'
    print('----------------')
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    print('----------------')
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12]\t{:^8}it{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


# 删除


def delete():
    while True:
        student_id = input('请输入需要删除的学生的id')
        if student_id != '':
            # 用于判断文件或目录是否存在，如果存在返回True, 否则返回False
            if os.path.exists(filename):
                # 上下文管理器打开
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                # 这里使用w覆盖是为了删除原来的数据 把原数据保存到新的字典 然后把需要删除的数据不导入txt文件里面
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 把字符串转化为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除后重新显示学生信息
            answer = input('是否继续删除?y/n\n')
            if answer == 'y':
                continue
            else:
                break


# 修改
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入需要修改的学生id: ')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息 可以修改')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['English'] = int(input('请输入英语成绩:'))
                        d['python'] = int(input('请输入python成绩:'))
                        d['java'] = int(input('请输入Java成绩: '))
                    except:
                        print('输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功!!!')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其它学生信息?y / n\n')
        if answer == 'y':
            modify()


def sort():
    pass


def total():
    if os.path.exists(filename):
        with open(filename, encoding='utf-8') as rflie:
            students = rflie.readlines()
            if students:
                print(f'一个有{len(students)}名学生')
            else:
                print('没有录入学生信息')
    else:
        print('暂无保存信息')


def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_lst=eval(item)
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存数据')


if __name__ == '__main__':
    main()
