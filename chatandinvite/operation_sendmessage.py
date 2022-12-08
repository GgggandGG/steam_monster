from chatandinvite.Strategy import Strategy
class operation_sendmessage(Strategy):
    def __init__(self,name,friend):
        self.__name=name
        self.__friend=friend

    def doopration(self):
        print("--------{0}---------".format(self.__name))
        while 1:
            print("send：(输入esc结束)")
            a=input()
            if a=="esc":
                print("聊天结束")
                break
            self.__friend.add_user_message(self.__name,a)
            print("发送成功")
        print("----------------------")