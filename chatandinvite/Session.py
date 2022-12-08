from abc import abstractmethod,ABCMeta
#Session接口
class Session(metaclass=ABCMeta):
    @abstractmethod
    def getHistory(self):
        pass

    @abstractmethod
    def excutestategy(self,context):
        pass