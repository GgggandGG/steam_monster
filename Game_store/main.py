from Game_browse_Factory import *
from Game_Window_Decorate import *
from User_and_Admin import *

def GameStore_main():
    user = User("gyh20083109")
    admin1 = Admin("admin1")
    game_factory = Game_Browse_Factory()
    game_1 = game_factory.create_game_browse("AdventureGame","超级玛丽","经典传统冒险游戏，作为一名管道工开启你的冒险吧","$45")
    game_2 = game_factory.create_game_browse("AdventureGame","穿越火线","作为一名雇佣兵，开启你在CF世界的冒险吧，生化酒店，巨人城，等你来战！","$0")
    game_3 = game_factory.create_game_browse("AdventureGame","造梦西游10","造梦的世界里，你我都是大闹天宫的孙悟空","$10")
    game_4 = game_factory.create_game_browse("CasualGame","星露谷物语","休闲游戏的经典之作，钓鱼、种田，一切由你经营","$50")
    game_5 = game_factory.create_game_browse("CasualGame","小鳄鱼洗澡","利用你的智慧，帮助小鳄鱼完成它的洗澡之旅吧","$5")
    game_6 = game_factory.create_game_browse("CasualGame","贪吃蛇","长长长！我还能再长！","$0")
    game_7 = game_factory.create_game_browse("Roleplay","古墓丽影","劳拉，即将出发！这次的目的地是秦始皇陵！","＄100")
    game_8 = game_factory.create_game_browse("Roleplay","赛尔号","扮演一个小塞尔，在茫茫的宇宙中带领你的精灵，挑战传说中的雷伊吧！","$30")
    game_9 = game_factory.create_game_browse("Roleplay","GTA10","源起侠盗猎车，这次我们将在火星开启我们的冒险","$100")
    game_10 = game_factory.create_game_browse("Roleplay","CS:GO","扮演维护正义的警察/残暴破坏的匪徒，你是谁，你来定义","$100")
    game_browse_list = [game_1,game_2,game_3,game_4,game_4,game_5,game_6,game_7,game_8,game_9,game_10]
    while(1):
        print("\n\n******商店******")
        print("1、创建游戏并上传"
              "\n2、浏览游戏商城并购买"
              "\n3、退回上一步"
              "\n请输入数字进行选择：")
        temp_input = input()
        if temp_input == "1":
            # 创建游戏窗口工厂
            browse_factory = Game_Browse_Factory()
            temp_input = input("请选择你想创建的游戏类型：\n 1、Adventure\n 2、Casual \n 3、Roleplay\n请输入:")
            # 创建冒险类游戏窗口
            if temp_input == "1":
                game_name = input("请输入游戏名：")
                game_info = input("请输入游戏介绍：")
                game_price = input("请输入游戏价格：")
                browse = browse_factory.create_game_browse("AdventureGame",game_name, game_info, game_price)
            # 创建休闲类游戏窗口
            elif temp_input == "2":
                game_name = input("请输入游戏名：")
                game_info = input("请输入游戏介绍：")
                game_price = input("请输入游戏价格：")
                browse = browse_factory.create_game_browse("CasualGame", game_name, game_info, game_price)
            # 创建角色扮演类游戏窗口
            else:
                game_name = input("请输入游戏名：")
                game_info = input("请输入游戏介绍：")
                game_price = input("请输入游戏价格：")
                browse = browse_factory.create_game_browse("RoleplayGame",game_name, game_info, game_price)
            temp_input = input("\n请选择装饰：\n1、**********装饰\n2、----------装饰\n3、不需要装饰\n请输入：")
            if temp_input == "1":
                decorator = WindowDecorate(browse)
                print("\n*****创建并装饰完成*****\n")
                # 装饰器装饰打印
                decorator.AddStars()
            elif temp_input == "2":
                decorator = WindowDecorate(browse)
                print("\n*****创建并装饰完成*****\n")
                # 装饰器装饰打印
                decorator.Addcrossing()
            else:
                print("\n*****创建并装饰完成*****\n")
                # 调用打印方法打印游戏上架信息
                browse.browse_print()
            proxy = Proxy("代理")
            print("\n即将通过代理为您发送至管理员进行审核：")
            proxy.send(browse,"Admin1",user)
            temp_input = input("请输入任意字符或字符串返回商店初始界面：")

        elif temp_input == "2":
            ###
            print("待完成")
        elif temp_input == "3":
            return 0
GameStore_main()
