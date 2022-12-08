class Wallet:
    def __init__(self):
        self.money = 0
    def invest(self,invest_money):
        self.money += invest_money
    def charge(self,charge):
        self.money -= charge
