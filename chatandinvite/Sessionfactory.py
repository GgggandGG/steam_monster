#工厂模式
from chatandinvite.Attainsession import Attainsession
class Sessionfactory():
    def __init__(self,name,frind):
        self.__name=name
        self.__frind=frind

    def createsession(self):
        return Attainsession(self.__name,self.__frind)