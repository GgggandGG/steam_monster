from chatandinvite.chatandinvite_main import chatandinvite
name = ['bob','alice','brown']
class TopRelation():
    def friend_menu(self):
        print("*       好友管理系统        *")
        print("---------------------------")
        print("*       1.添加好友         *")
        print("*       2.删除好友         *")
        print("*       3.显示好友         *")
        print("*       4.退出系统         *")
        print("*       5.显示日志         *")
        print("---------------------------")
    def friend_add(self):
        num_1 = input("请输入添加好友邮箱：")
        name.append(num_1)
        print("添加成功")
    def friend_del(self):
        del_name = input("请输入删除好友姓名：")

        print("*            确认删除？          *")
        print("*                              *")
        print("*       1.确认    2.取消         *")
        num_2= input("请输入序号：")
        if num_2 == "1":
            name.remove(del_name)
            print("删除成功！")
        elif num_2 == "2":
            print("取消成功！")
    def friend_show(self):
        print("*         好友列表         *")
        print("---------------------------")
        print("*      1.进入聊天系统       *")
        for i in name:
            print("         "+i+"         ")
        print("*      2.退出好友系统       *")
        print("---------------------------")
        num_3 = int(input("请输入序号："))
        if num_3 ==1:
            personname = input("请输入姓名:")
            chatandinvite(personname)
        elif num_3 ==2:
            quit()
