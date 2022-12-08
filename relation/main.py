from relation import TopRelation
from LoggerFactory import *
# Press the green button in the gutter to run the script.
def relation_main():
    TopRelation1 = TopRelation()
    while(True):
        TopRelation1.friend_menu()
        num = int(input("请输入序号："))
        if num == 1:
            TopRelation1.friend_add()
        elif num == 2:
            TopRelation1.friend_del()
        elif num == 3:
            TopRelation1.friend_show()
        elif num == 4:
            break
        elif num == 5:
            logger = Logger(__name__).get_logger()
            logger.info("==========\n")
relation_main()