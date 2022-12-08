from market.proxy2 import proxy2


def market():
    while 1:
        print("-----------------")
        print("请选择您要使用的功能：")
        print("1.出售物品")
        print("2.购买物品")
        print("3.查看交易信息")
        option = input()
        if option == 0:
            break
        else:
            P = proxy2(option)
            P.function()

# market()