#工厂模式
from Attainsession import Attainsession
class Sessionfactory():
    def __init__(self,name):
        self.__name=name

    def createsession(self):
        return Attainsession(self.__name)