class Wallet:
    def __init__(self):
        self.money = 0.0
    def invest(self,invest_money):
        if not isinstance(invest_money,float) and not isinstance(invest_money,int):
            print("参数错误，请给出浮点数或整数参数")
        elif invest_money < 0:
            print("参数错误，传入参数必须大于等于0")
        else:
            self.money += invest_money
    def charge(self,charge):
        self.money -= charge
