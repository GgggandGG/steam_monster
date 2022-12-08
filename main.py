import time

from login.login import login_main
from relation.main import relation_main
from Game_store.Gamestore_main import *
from gamelibrary.gamelibrary_Server import *
from market.main import market
from Game_Wallet.wallet_main import Gamewallet_main
# 全局钱包实例
wallet = Wallet()

if __name__ == "__main__":
    login_main()
    while(1):
        print("\n**********主界面**********")
        print("1、好友\n"
              "2、游戏商店\n"
              "3、我的游戏\n"
              "4、交易市场\n"
              "5、钱包\n"
              "6、退出steam")
        temp_input = input("请输入序号进行下一步：")
        if temp_input == "1":
            pass
            relation_main()
        elif temp_input == "2":
            GameStore_main(wallet)
        elif temp_input == "3":
            gamelibrary()
        elif temp_input == "4":
            market()
        elif temp_input == "5":
            Gamewallet_main(wallet)
        elif temp_input == "6":
            break
        else:
            print("输入错误，请重新操作......")
            time.sleep(1)