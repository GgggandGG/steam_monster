from market.mart import mart
from market.user import user

M = mart()
date = "2022.12.06"
uname = 'yfy'
U = user(uname)

class proxy2():
    def __init__(self, option):
        self.option = option

    def function(self):
        if self.option =='1':
            U.showhouse()
            print("请输入您想售卖的物品的名称：")
            name = input()
            print("请输入您为该物品定的单价：")
            price = int(input())
            print("请输入您想出售该物品的数量：")
            num = int(input())
            seller = None
            flag = U.sell(name, num, price, date, seller)
            if flag == 1:
                M.PutOnSale(name, price, uname, num)
        elif self.option =='2':
            M.show()
            print("请输入您想购买的商品的编号：")
            index = int(input())
            print("请输入您想购买该商品的数量：")
            num = int(input())
            name = M.goods[index][0]
            price = M.goods[index][1]
            seller = M.goods[index][2]
            flag = M.sell(index, num)
            if flag == 1:
                U.buy(name, num, price, date, seller)
        elif self.option =='3':
            print("请选择：")
            print("1.查看已出售物品：")
            print("2.查看订购单：")
            print("3.查看交易记录")
            option = input()
            U.check(option)
        else:
            print("请输入正确选项")