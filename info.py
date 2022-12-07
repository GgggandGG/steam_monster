class informations():
    def __init__(self, uname):
        self.uname = uname
        self.tradecodes = [["aaa", -5, "2022.12.05"], ["bbb", 3, "2002.12.04"]]  # 交易记录 name, sum(金额，买为负，卖为正), date
        self.soldgoods = [["ccc", 2, 10], ["ooo", 4, 20]]  # 已出售物品 name, price, num
        self.buingorders = [["sss", 3, 2, 6, "yfy", "2022.12.05"], ["zzz", 5, 1, 5, "yfy", "2022.12.04"]]
        # 订购单 name, price, num, sum(都为买，不以正负区分，都为正), seller, date

    def update(self, name, price, date, num, seller):
        sum = price * num
        if seller == None:
            self.tradecodes.append([name, sum, date])
            self.soldgoods.append([name, price, num])
        else:
            self.tradecodes.append([name, -sum, date])
            self.buingorders.append([name, price, num, sum, seller, date])

    def printout1(self):
        print("已出售物品：")
        print("物品名称 出售单价 出售数量")
        for i in self.soldgoods:
            print(i)

    def printout2(self):
        print("订购单:")
        print("物品名称 买入单价 买入数量 买入总价 卖家 日期")
        for i in self.buingorders:
            print(i)

    def printout3(self):
        print("交易记录：")
        print("物品名称 收入/支出 日期")
        for i in self.tradecodes:
            print(i)

# ii = informations("yfy")
# ii.update("xx", 5, "2022.12.5", 3, 'yff')
# ii.printout1()
# ii.printout2()
# ii.printout3()