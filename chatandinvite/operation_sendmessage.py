from Strategy import Strategy
class operation_sendmessage(Strategy):
    def doopration(self):
        print("--------{0}---------".format(self.name))
        while 1:
            print("send：(输入esc结束)")
            a=input()
            if a=="esc":
                print("聊天结束")
                break
            print("发送成功")
        print("----------------------")