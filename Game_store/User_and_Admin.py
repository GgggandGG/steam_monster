class User:
    def __init__(self,user_name):
        self.user_name = user_name
    def send(self,browse_window,user_name):
        pass
    def receive(self,user_name):
        pass
    def Buy(self):
        pass

# 用户代理
class Proxy(User):
    def __init__(self,user_name):
        super().__init__(user_name)
    def send(self,browse_window,receive_user_name,send_user:User):
        print(f"\n发送方：{send_user.user_name}"
              f"\n接收方：{receive_user_name}"
              f"\n发送信息：")
        browse_window.browse_print()
    def receive(self,user_name):
        pass

class Admin(User):
    def __init__(self,user_name):
        super().__init__(user_name)
        self.games_to_audit = []
    def send(self,browse_window,user_name):
        print(f"\n发送方：{self.user_name}"
              f"接收方：{user_name}"
              f"发送信息：")
        browse_window.browse_print()
    def receive(self,user_name):
        pass
    def audit(self):
        for game in self.games_to_audit:
            game.browse_print()
            temp_input = input("请输入(pass/reject)：")
            if temp_input == "pass":
                print("审核通过")
            else:
                print("审核不通过")



