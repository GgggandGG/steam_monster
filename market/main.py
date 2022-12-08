from market.mart import mart
from market.user import user

def market():
    M = mart()
    date = "2022.12.06"
    uname = 'yfy'
    U = user(uname)
    while 1:
        print("-----------------")
        print("请选择您要使用的功能：")
        print("1.出售物品")
        print("2.购买物品")
        print("3.查看交易信息")
        option = input()

        if option =='1':
            U.showhouse()
            print("请输入您想售卖的物品的名称：")
            name = input()
            print("请输入您为该物品定的单价：")
            price = int(input())
            print("请输入您想出售该物品的数量：")
            num = int(input())
            seller = None
            U.sell(name, num, price, date, seller)
            M.PutOnSale(name, price, uname, num)
        elif option =='2':
            M.show()
            print("请输入您想购买的商品的编号：")
            index = int(input())
            print("请输入您想购买该商品的数量：")
            num = int(input())
            name = mart.goods[index][0]
            price = mart.goods[index][1]
            seller = mart.goods[index][2]
            M.sell(index, num)
            U.buy(name, num, price, date, seller)
        elif option =='3':
            print("请选择：")
            print("1.查看已出售物品：")
            print("2.查看订购单：")
            print("3.查看交易记录")
            option = input()
            U.check(option)
        elif option =='0':
            break
        else:
            print("请输入正确选项")