# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
name = []
def friend_menu():
    print("*       好友管理系统        *")
    print("---------------------------")
    print("*       1.添加好友         *")
    print("*       2.删除好友         *")
    print("*       3.显示好友         *")
    print("*       4.返回系统         *")
    print("---------------------------")
def friend_add():
    num_1 = input("请输入添加好友邮箱：")
    name.append(num_1)
    print("添加成功")
def friend_del():
    del_name = input("请输入删除好友姓名：")

    print("*            确认删除？          *")
    print("*                              *")
    print("*       1.确认    2.取消         *")
    num_2= input("请输入序号：")
    if num_2==1:
        name.remove(del_name)
        print("删除成功！")
    elif num_2==2:
        print("取消成功！")
def friend_show():
    for i in name:
        print(i)
# def back():

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(True):
        friend_menu()
        num = int(input("请输入序号："))
        if num == 1:
            friend_add()
        elif num == 2:
            friend_del()
        elif num == 3:
            friend_show()
        # elif num == 4:
        #     back()

