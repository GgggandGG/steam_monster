from chatandinvite.Session import Session
#实现session接口
class Attainsession(Session):
    def __init__(self,name,frind):
        self.__name=name
        self.__frind = frind

    def getHistory(self):
        self.__frind.print_user_message(self.__name)

    def excutestategy(self,strategy):
        strategy.doopration()