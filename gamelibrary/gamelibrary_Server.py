from gamelibrary.game import games_list, games_id, games_name
from gamelibrary.gamecommunity import gamecommunity
from gamelibrary.gamelibrary import Library
from gamelibrary.gametogether import play_together
def gamelibrary():
    userid=1 #根据用户id获取其对应的库
    user_library=Library(userid,games_list)
    while(1):
        print("***************************************")
        print("您的游戏库:(请输入游戏id进行游玩或其他操作)")
        user_library.listgames()
        print("**************************输入quit退出库**")
        input1=input()
        option_game=eval(input1)
        if input1=="quit":
            break
        if option_game in games_id:
            print("***************************************")
            print(games_name[option_game-1])
            print("1.本地游玩")
            print("2.远程畅玩")
            print("3.游戏社区")
            print("***************************************")
            input2=input()
            if input2 == "quit":
                break
            if input2== "1":

                print("开始游玩" + games_name[option_game - 1])
                print("读取游戏文件中。。。")
                print("***************************************")
                print("*                                     *")
                print("*                 " + games_name[option_game - 1])
                print("*                                     *")
                print("***************************************")
                temp_input = input("输入任意字符退出")
            elif input2=="2":
                play_together()
                temp_input = input("输入任意字符退出")
            elif input2 == "3":
                print(games_name[option_game - 1] + "社区 ")
                gamecommunity()

            else:
                print("请输入正确的指令")
        else:
            print("请输入正确的指令")