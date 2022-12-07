from Game_browse_Factory import *

# 窗口装饰器
class WindowDecorate:
    def __init__(self,browse_window):
        self.browse_window = browse_window
    # 前后用*包裹
    def AddStars(self):
        print("\n**********")
        self.browse_window.browse_print()
        print("\n**********")
    # 前后用-包裹
    def Addcrossing(self):
        print("\n----------")
        self.browse_window.browse_print()
        print("\n----------")

if __name__ == "__main__":
    browse_window = AdventureGame_Browse("1","2","3")
    decorator = WindowDecorate(browse_window)
    decorator.Addcrossing()
    decorator1 = WindowDecorate(browse_window)
    list_obj = []
    list_obj.append(decorator)



