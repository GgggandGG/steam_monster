import random
import time

from Game_Wallet.Gamewallet import *


def Gamewallet_main(wallet):
    while(1):
        print("\n*****钱包*****")
        temp_input = input("1、查看钱包余额\n2、钱包充值\n3、返回主界面\n请输入序号：")
        if temp_input == "1":
            print(f"\n钱包余额：${wallet.money}")
            temp_input = input("输入任意键退回上一步")
        elif temp_input == "2":
            while(1):
                temp_input = input("\n请输入想要充值的金额（整数）:")
                if temp_input.isdigit():
                    print("正在生成订单......")
                    time.sleep(1)
                    print("已发送支付订单至邮箱，等待支付中......")
                    time.sleep(5)
                    rand = random.random()
                    if rand > 0.2:
                        wallet.invest(float(temp_input))
                        print("支付成功")
                        print(f"钱包余额：${wallet.money}")
                        time.sleep(2)
                    else:
                        print("支付失败，请重新充值...")
                        time.sleep(2)
                    break
                else:
                    print("输入错误，请重新输入")
                    time.sleep(2)

        elif temp_input == "3":
            return 0
        else:
            print("输入错误！请重新选择")