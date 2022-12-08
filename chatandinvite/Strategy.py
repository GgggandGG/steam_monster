from abc import abstractmethod,ABCMeta
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def doopration(self):
        pass