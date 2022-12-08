import time

from Game_store.Game_browse_Factory import *
from Game_store.Game_Window_Decorate import *
from Game_store.User_and_Admin import *
from Game_store.Game_DB import game_DB
from Game_store.Game_DB import Local_Game_store
from Game_store.Buy_strategy import *


def GameStore_main(wallet):
    user = User("gyh20083109")
    admin1 = Admin("admin1")
    game_factory = Game_Browse_Factory()
    game_1 = game_factory.create_game_browse("AdventureGame","超级玛丽","经典传统冒险游戏，作为一名管道工开启你的冒险吧",45)
    game_2 = game_factory.create_game_browse("AdventureGame","穿越火线","作为一名雇佣兵，开启你在CF世界的冒险吧，生化酒店，巨人城，等你来战！",0)
    game_3 = game_factory.create_game_browse("AdventureGame","造梦西游10","造梦的世界里，你我都是大闹天宫的孙悟空",10)
    game_4 = game_factory.create_game_browse("CasualGame","星露谷物语","休闲游戏的经典之作，钓鱼、种田，一切由你经营",50)
    game_5 = game_factory.create_game_browse("CasualGame","小鳄鱼洗澡","利用你的智慧，帮助小鳄鱼完成它的洗澡之旅吧",5)
    game_6 = game_factory.create_game_browse("CasualGame","贪吃蛇","长长长！我还能再长！",0)
    game_7 = game_factory.create_game_browse("Roleplay","古墓丽影","劳拉，即将出发！这次的目的地是秦始皇陵！",100)
    game_8 = game_factory.create_game_browse("Roleplay","赛尔号","扮演一个小塞尔，在茫茫的宇宙中带领你的精灵，挑战传说中的雷伊吧！",30)
    game_9 = game_factory.create_game_browse("Roleplay","GTA10","源起侠盗猎车，这次我们将在火星开启我们的冒险",100)
    game_10 = game_factory.create_game_browse("Roleplay","CS:GO","扮演维护正义的警察/残暴破坏的匪徒，你是谁，你来定义",100)
    game_browse_list = [game_1,game_2,game_3,game_4,game_5,game_6,game_7,game_8,game_9,game_10]
    local_game_store = Local_Game_store()
    # 将本地商店作为观察者链接到游戏数据库
    game_DB.attach(local_game_store)
    game_DB.init_gamelist(game_browse_list)
    while(1):
        print("\n******商店******")
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
            game_DB.add_game(browse)
            temp_input = input("请输入任意字符或字符串返回商店初始界面：")

        elif temp_input == "2":
            while(1):
                print("**********游戏列表**********")
                local_game_store.game_list_print()
                temp_input = input("输入你想了解的游戏编号或输入quit退回到上个界面：")
                if temp_input == "quit":
                    break
                elif int(temp_input) > 0 & int(temp_input) < local_game_store.list_len+1:
                    browse = local_game_store.get_game_and_print(int(temp_input))
                    temp_input = input("\n输入1：购买此游戏\n输入其他任意字符：返回到游戏列表\n请输入：")
                    if temp_input != "1":
                        continue
                    if temp_input == "1":
                        temp_string = f"\n请选择购买策略：\n1、购买体验版(price：${browse.game_price*0.1})\n2、购买月付版(price：${browse.game_price*0.4})\n3、购买完整版(price：${browse.game_price})\n4、放弃购买\n请输入选择:"
                        temp_input = input(temp_string)
                        if temp_input == "1":
                            buy_context = BuyContext(ExperienceBuy(wallet))
                            buy_context.charge(browse)
                        elif temp_input == "2":
                            buy_context = BuyContext(MonthlyBuy(wallet))
                            buy_context.charge(browse)
                        elif temp_input == "3":
                            buy_context = BuyContext(TotalBuy(wallet))
                            buy_context.charge(browse)
                        else:
                            print("放弃购买此游戏中...")
                            time.sleep(2)
                else:
                    print("没有对应编号或quit，请重新选择并输入")

        elif temp_input == "3":
            return 0

