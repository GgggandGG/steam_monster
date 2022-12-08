from abc import abstractmethod,ABCMeta
class Strategy(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def doopration(self):
        pass