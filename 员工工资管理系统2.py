# _*_ coding=utf-8 _*_
# __Author__ = 张泽林
import os


def worker_file_switch():  # 转换员工文件为字典
    all_worker_dict = {}
    with open('info.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith('\n'):
                name, salary = line.strip().split(' ')
                all_worker_dict[name] = int(salary)
    return all_worker_dict


def worker_view_all():  # 查询所有员工列表
    for line in worker_file_switch():
        print('|----姓名：%s----|' % line)


def file_remove_rename():  # 文件的覆盖
    os.remove('info.txt')
    os.rename('info_new.txt', 'info.txt')


def worker_search():  # 查询员工信息，用到字典[1、判断员工是否存在2、取字典的KEY和相应的参数(工资)]
    user_input_data = str(input('请选择要查询的员工名称>>>>').strip())
    if len(user_input_data) == 0 or user_input_data not in worker_file_switch():
        print('-----\033[33;1m该员工信息不存在，请重新输入\033[0m-----')
    else:
        print('员工\033[31;1m%s\033[0m的工资为\033[32;1m%s\033[0m'
              % (user_input_data, worker_file_switch().setdefault(user_input_data)))


def worker_fix():  # 修改员工工资信息,用到字典[判断员工是否存在]
    user_input_data = input('输入格式[\033[35;1m姓名\033[0m \033[36;1m工资\033[0m]>>>>')
    user_input_name = user_input_data.strip().split(' ')
    if len(user_input_data) == 0 or user_input_name[0] not in worker_file_switch():
        print('-----\033[33;1m该员工信息不存在，请重新输入\033[0m-----')
    else:
        with open('info.txt', 'r', encoding='utf-8') as f, \
                open('info_new.txt','w',encoding='utf-8') as new_f:
            for line in f:
                if not line.startswith(user_input_name[0]):
                    new_f.write(line)
                else:
                    new_f.write(user_input_data.strip() + '\n')
        file_remove_rename()
        print('-----\033[34;1m修改成功\033[0m-----')


def worker_append():  # 增加新用户，用到字典在特定位置显示员工姓名
    user_input_data = str(input('输入格式[\033[35;1m姓名\033[0m \033[36;1m工资\033[0m]>>>>').strip())
    user_input_name = user_input_data.strip().split(' ')
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('\n')
        f.write(user_input_data)
    print('-----\033[34;1m增加新员工%s成功\033[0m-----' % user_input_name[0])


def worker_remove():  # 增加新用户，用到字典在特定位置显示员工姓名
    user_input_data = str(input('请选择要删除的员工名称>>>>').strip())
    user_input_name = user_input_data.strip().split(' ')
    with open('info.txt', 'r', encoding='utf-8') as f, \
            open('info_new.txt', 'w', encoding='utf-8') as new_f:
        for line in f:
            if not line.startswith(user_input_name[0]):
                new_f.write(line)
            else:
                continue
    file_remove_rename()
    print('-----\033[34;1m删除新员工%s成功\033[0m-----' % user_input_name[0])

if __name__ == '__main__':
    worker_list = '''
    1:查询员工工资
    2:修改员工工资
    3:增加新员工记录
    4:删除员工记录
    5:显示在职员工列表
    6:退出系统
    '''
    operands = {
        '1': worker_search,
        '2': worker_fix,
        '3': worker_append,
        '4': worker_remove,
        '5': worker_view_all,
        '6': exit
    }
    while True:
        print(worker_list)
        user_input_SN = input('请选择操作方式>>>>')
        if len(user_input_SN) == 0 or user_input_SN not in operands:
            print('-----\033[33;1m输入的信息有误，请重新选择-----\033[0m')
            continue
        elif user_input_SN == '6':
            break
        else:
            operands[user_input_SN]()
