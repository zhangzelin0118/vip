# _*_ coding=utf-8 _*_

def worker_search(user_input_data):
    worker_search_list = [] #定义空列表，存放筛选的数据
    with open('info.txt', 'r', encoding="utf-8") as search_f: #打开文件
        for line in search_f: #循环文件，读每行信息
            if line.startswith(user_input_data): #判断，如果用户输入的数据在该行，把该行放入空列表
                worker_search_list.append(line.strip())
            else:
                pass
        print(worker_search_list)
        list = "".join(worker_search_list)
        list2 = list.split()
        print(list)
        print(list2)
        for line2 in worker_search_list:
            print(line2)
        #return worker_search_list
def worker_fix(user_input_data):
    worker_fix_list = worker_search(user_input_data)
    choice = input("请输入要修改的员工信息>>>>")
    if user_input_data in worker_fix_list:
        print("相同名称,")
def worker_append(user_input_data):
    print('this is append')

if __name__ == '__main__':
    worker_list = '''
    1:查询员工工资
    2:修改员工工资
    3:增加新员工记录
    4:退出系统
    '''
    operands = {
        '1': worker_search,
        '2': worker_fix,
        '3': worker_append,
        '4': exit
    }
    while True:
        print(worker_list)
        user_input_SN = input('请选择操作方式>>>>')
        if len(user_input_SN) == 0 or user_input_SN not in operands:
            print('-----\033[31;1m输入的信息有误，请重新选择-----\033[0m')
            continue
        elif user_input_SN == '4':
            break
        else:
            user_input_data = input('请输入数据')
            operands[user_input_SN](user_input_data)