class warehouse():
    def __init__(self, uname):
        self.uname = uname
        self.__goods = [["lifeline", 2], ["plague", 3]]

    def buyin(self, name, num):
        flag = 0
        for i in self.__goods:
            if i[0] == name:
                i[1] = i[1]+num
                flag == 1
                print("您已成功购买该物品！")
                break
        if flag == 0:
            self.__goods.append([name, num])

    def sellout(self, name, num):
        flag = 0
        for i in self.__goods:
            if i[0] == name:
                flag = 1
                if num <= i[1]:
                    i[1] = i[1]-num
                    print("您已成功出售该物品！")
                else:
                    print("您的仓库中没有那么多库存")
                break
        if flag == 0:
            print("您的仓库中没有该物品！")

    def show(self):
        print("仓库：")
        print("物品名称 拥有数量")
        for i in self.__goods:
            print(i)

# ww = warehouse("yfy")
# ww.buyin("life", 1)
# ww.sellout("lifeline", 2)
# ww.show()
