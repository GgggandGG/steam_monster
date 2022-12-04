from Sessionfactory import Sessionfactory
from Context import Context
from operation_sendmessage import operation_sendmessage
from operation_invitegame import operation_invitegame
while 1:
    print("-----------------")
    print("请选择您要使用的功能：")
    print("1.发送消息")
    print("2.游戏邀请")
    print("3.查看聊天记录")
    print("-----------------")
    name = '1'
    option=input()
    sessionfactory = Sessionfactory(name)
    attanseesion = sessionfactory.createsession()

    if option=='1':
        context = Context(attanseesion,operation_sendmessage(name))
        context.excutestategy()
    elif option=='2':
        context = Context(attanseesion,operation_invitegame(name))
        context.excutestategy()
    elif option=='3':
        context = Context(attanseesion)
        context.doAttainsession()
    elif option=='0':
        break
    else :
        print("请输入正确选项")