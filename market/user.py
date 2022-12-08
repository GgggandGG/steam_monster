from market.proxy1 import proxy1

class user():
    def __init__(self, uname):
        self.Proxy = proxy1(uname)

    def showhouse(self):
        self.Proxy.showhouse()

    def buy(self, name, num, price, date, seller):
        self.Proxy.buy(name, num, price, date, seller)

    def sell(self, name, num, price, date, seller ):
        flag = self.Proxy.sell(name, num, price, date, seller)
        return flag

    def check(self, option):
        self.Proxy.check(option)