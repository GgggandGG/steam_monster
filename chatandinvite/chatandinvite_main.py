from chatandinvite.Sessionfactory import Sessionfactory
from chatandinvite.operation_sendmessage import operation_sendmessage
from chatandinvite.operation_invitegame import operation_invitegame
def chatandinvite(name):
    while 1:
        print("-----------------")
        print("请选择您要使用的功能：")
        print("1.发送消息")
        print("2.游戏邀请")
        print("3.查看聊天记录")
        print("-----------------")
        option = input()
        sessionfactory = Sessionfactory(name)
        attanseesion = sessionfactory.createsession()
        if option == '1':
            attanseesion.excutestategy(operation_sendmessage(name))
        elif option == '2':
            attanseesion.excutestategy(operation_invitegame(name))
        elif option == '3':
            attanseesion.getHistory()
        elif option == '0':
            break
        else:
            print("请输入正确选项")
chatandinvite('bob')