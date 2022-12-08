from chatandinvite.Session import Session
from chatandinvite.friend_info import frind_info
#实现session接口
class Attainsession(Session):
    def __init__(self,name):
        self.__name=name
        self.__frind = frind_info()

    def getHistory(self):
        self.__frind.print_user_message(self.__name)

    def excutestategy(self,context):
        context.doopration()