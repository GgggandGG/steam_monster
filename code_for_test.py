import unittest
from Game_Wallet.Gamewallet import Wallet
import random
import numpy as np

wallet = Wallet()
class WalletTestCase(unittest.TestCase):
    """测试Wallet类的方法"""

    # 测试充值函数
    # 浮点数输入测试
    def test_invest_input_float(self):
        x = random.random()
        wallet.invest(x)
        self.assertTrue(isinstance(wallet.money, float))

    # 字符串输入测试
    def test_invest_input_string(self):
        # 字符串输入测试
        x = " "
        wallet.invest(x)
        self.assertTrue(isinstance(wallet.money, float))

    # 列表输入测试
    def test_invest_input_list(self):
        x = [1,2,3]
        wallet.invest(x)
        self.assertTrue(isinstance(wallet.money, float))

    # 各种float或int类型数据输入
    def test_invest_num(self):
        x = random.randint(-99999,99999)
        e = np.power(10,random.randint(-5,5))
        x = x/e
        wallet.invest(x)
        self.assertTrue(wallet.money >= 0)

if __name__ == "__main__":
    unittest.main()


