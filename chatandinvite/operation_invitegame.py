from chatandinvite.Strategy import Strategy
from gamelibrary.game import games_list

class operation_invitegame(Strategy):
    def doopration(self):
        print("请选择您的游戏：")
        for i in games_list:
            print(i)
        a = input()
        print("邀请已发送")