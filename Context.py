class Context:
    def __init__(self,Attainsession,strategy=None):
        self.__strategy = strategy
        self.__attainsession=Attainsession

    def excutestategy(self):
        self.__strategy.doopration()

    def doAttainsession(self):
        self.__attainsession.getHistory()