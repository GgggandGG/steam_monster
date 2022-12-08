from chatandinvite.Sessionfactory import Sessionfactory
from chatandinvite.operation_sendmessage import operation_sendmessage
from chatandinvite.operation_invitegame import operation_invitegame
from chatandinvite.friend_info import frind_info
def chatandinvite(name):
    frind = frind_info()
    while 1:
        print("-----------------")
        print("请选择您要使用的功能：")
        print("1.发送消息")
        print("2.游戏邀请")
        print("3.查看聊天记录")
        print("0.结束聊天")
        print("-----------------")
        option = input()
        sessionfactory = Sessionfactory(name,frind)
        attanseesion = sessionfactory.createsession()
        if option == '1':
            attanseesion.excutestategy(operation_sendmessage(name,frind))
        elif option == '2':
            attanseesion.excutestategy(operation_invitegame())
        elif option == '3':
            attanseesion.getHistory()
        elif option == '0':
            break
        else:
            print("请输入正确选项")