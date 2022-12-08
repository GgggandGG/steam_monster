from market.info import informations
from market.warehouse import warehouse

class user():
    def __init__(self, uname):
        self.WareHouse = warehouse(uname)
        self.Information = informations(uname)

    def showhouse(self):
        self.WareHouse.show()

    def buy(self, name, num, price, date, seller):
        self.WareHouse.buyin(name, num)
        self.Information.update(name, price, date, num, seller)

    def sell(self, name, num, price, date, seller ):
        self.WareHouse.sellout(name, num)
        self.Information.update(name, price, date, num, seller)

    def check(self, option):
        if option=='1':
            self.Information.printout1()
        elif option=='2':
            self.Information.printout2()
        elif option == '3':
            self.Information.printout3()
        else:
            print("请输入正确选项")