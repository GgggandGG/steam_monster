import time

class Wallet:
    def __init__(self):
        self.money = 0
    def invest(self,invest_money):
        self.money += invest_money
    def charge(self,charge):
        self.money -= charge

class Buy:
    def __init__(self,wallet):
        self.wallet = wallet
    def buy(self,price):
        pass

class ExperienceBuy(Buy):
    def __init__(self,wallet):
        super().__init__(wallet)
    def buy(self,price):
        payment = price*0.1
        print(f"钱包余额：${self.wallet.money}    需付款：${payment}")
        if payment > self.wallet.money:
            print("余额不足，请联系管理员进行充值")
            time.sleep(3)
        else:
            self.wallet.charge(payment)
            print(f"购买成功！购买后钱包余额：${self.wallet.money}")
            time.sleep(3)

class MonthlyBuy(Buy):
    def __init__(self,wallet):
        super().__init__(wallet)
    def buy(self,price):
        payment = price*0.4
        print(f"钱包余额：${self.wallet.money}    需付款：${payment}")
        if payment > self.wallet.money:
            print("余额不足，请联系管理员进行充值")
            time.sleep(3)
        else:
            self.wallet.charge(payment)
            print(f"购买成功！购买后钱包余额：${self.wallet.money}")
            time.sleep(3)

class TotalBuy(Buy):
    def __init__(self,wallet):
        super().__init__(wallet)
    def buy(self,price):
        payment = price
        print(f"$钱包余额：{self.wallet.money}    需付款：${payment}")
        if payment > self.wallet.money:
            print("余额不足，请联系管理员进行充值")
            time.sleep(3)
        else:
            self.wallet.charge(payment)
            print(f"购买成功！购买后钱包余额：${self.wallet.money}")
            time.sleep(3)

class BuyContext:
    def __init__(self,buyinstance):
        self.buy_instance = buyinstance
    def charge(self,browse):
        self.buy_instance.buy(browse.game_price)
