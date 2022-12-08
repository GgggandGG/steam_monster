class mart():
    def __init__(self):
        self.goods = [["lifeline", 3.5, "yfy", 5], ["plague", 4.5, "yff", 6]]

    def PutOnSale(self, name, price, seller, num):
        self.goods.append([name, price, seller, num])

    def soldout(self):
        for i in self.goods:
            if i[3] == 0:
                self.goods.remove(i)

    def sell(self, index, num):
        i = self.goods[index]
        if i[3] >= num:
            i[3] = i[3] - num
            return 1;
        else:
            print("库存不够，请减少购买数量")
            return 0;
        self.soldout()

    def show(self):
        print("市场：")
        print("商品编号 物品名称 单价 卖家 库存")
        j = 0
        for i in self.goods:
            print(j, i)
            j = j + 1

# mm = mart()
# mm.show()