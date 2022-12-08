# 游戏窗口
class Game_Browse_Window():
    def __init__(self, game_name, game_info, game_price):
        self.game_name = game_name
        self.game_info = game_info
        self.game_price = game_price

    def browse_print(self):
        print(f"游戏名：{self.game_name}")
        print(f"游戏信息:"
              f"{self.game_info}\n"
              f"游戏价格:${self.game_price}")

# 冒险类游戏窗口
class AdventureGame_Browse(Game_Browse_Window):
    def __init__(self, game_name, game_info, game_price):
        super().__init__(game_name, game_info, game_price)
        self.game_type = "Adventure"

# 休闲类游戏窗口
class CasualGame_Browse(Game_Browse_Window):
    def __init__(self, game_name, game_info, game_price):
        super().__init__(game_name, game_info, game_price)
        self.game_type = "Casual"

# 角色扮演类游戏窗口
class RoleplayGame_Browse(Game_Browse_Window):
    def __init__(self, game_name, game_info, game_price):
        super().__init__(game_name, game_info, game_price)
        self.game_type = "Roleplay"

# 游戏窗口工厂
class Game_Browse_Factory():
    def create_game_browse(self, type, game_name, game_info, game_price):
        if type=="AdventureGame":
            return AdventureGame_Browse(game_name,game_info,game_price)
        elif type == "CasualGame":
            return CasualGame_Browse(game_name,game_info,game_price)
        elif type == "Roleplay":
            return RoleplayGame_Browse(game_name,game_info,game_price)
        else:
            print("Create Error! No such type of game!")
            return None



if __name__ == '__main__':
    game_browse_factory = Game_Browse_Factory()
    adven_browse = game_browse_factory.create_game_browse("AdventureGame","地下城与勇士","动作冒险游戏","35$")
    adven_browse.browse_print()
