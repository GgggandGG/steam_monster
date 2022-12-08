from gamelibrary.game import Game, games_list, games_id, games_name
from gamelibrary.gametogether import play_together

class Library(Game):
    def __init__(self,id,games_list):
        self.userid=id
        self.games_list=games_list

    def listgames(self):
        for i in self.games_list:
            print(i)





