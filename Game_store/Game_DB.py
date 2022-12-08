# 数据库类
class Game_DB:
    def __init__(self,game_list=None):
        if game_list == None:
            self.game_list = []
        else:
            self.game_list = game_list
        self.local_game_stores_observers = []
    def attach(self,observer):
        self.local_game_stores_observers.append(observer)
    def deattach(self,observer):
        self.local_game_stores_observers.remove(observer)
    # 通知观察者
    def notify(self):
        for item in self.local_game_stores_observers:
            item.update(self.game_list)
    # 初始化游戏列表
    def init_gamelist(self,game_list):
        self.game_list = game_list
        self.notify()
    # 添加游戏
    def add_game(self,browse_window):
        if browse_window not in self.game_list:
            self.game_list.append(browse_window)
            self.notify()

# 创建单例对象
game_DB = Game_DB()

# 本地游戏商城
class Local_Game_store():
    def __init__(self,game_list=None):
        if game_list == None:
            self.game_list = []
        else:
            self.game_list = game_list
        self.list_len = len(self.game_list)
    def update(self,game_list):
        print("正在更新游戏商店游戏......")
        print("更新成功！")
        self.game_list = game_list
        self.list_len = len(game_list)

    def game_list_print(self):
        for i in range(self.list_len):
            print(f"{i+1}、游戏名称：{self.game_list[i].game_name}      游戏价格：${self.game_list[i].game_price}")
        print("***************")

    def get_game_and_print(self,num):
        self.game_list[num-1].browse_print()
        return self.game_list[num-1]