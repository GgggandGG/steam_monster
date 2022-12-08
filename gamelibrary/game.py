class Game:
  def __init__(self,gameid, gamename):
    self.__gameid = gameid
    self.__gamename = gamename

  def list(self):
    #print(str(self.gameid)+ ". "+self.gamename)
    return str(str(self.__gameid)+ ". "+self.__gamename)

  def getgames_id(self):
    return  self.__gameid
  def getgames_name(self):
    return  self.__gamename

game1=Game(1,"csgo")
game2=Game(2,"witch it!")
game3=Game(3,"cod19")

games_id=[]
games_id.append(game1.getgames_id())
games_id.append(game2.getgames_id())
games_id.append(game3.getgames_id())

games_name=[]
games_name.append(game1.getgames_name())
games_name.append(game2.getgames_name())
games_name.append(game3.getgames_name())

games_list=[game1.list(),game2.list(),game3.list()]


