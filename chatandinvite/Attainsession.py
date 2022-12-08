from Session import Session
#实现session接口
class Attainsession(Session):
    def __init__(self,name):
        self.__name=name
        self.__history=["在吗","我喜欢你","再见"]

    def getHistory(self):
        for i in self.__history:
            print(i)

    def excutestategy(self,context):
        context.doopration()