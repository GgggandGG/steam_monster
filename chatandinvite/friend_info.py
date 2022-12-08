class frind_info():
    def __init__(self):
        self.__friend_name=['bob','alice','brown']
        self.__friend_message={i:[] for i in self.__friend_name}

    def add_user(self,name):
        self.__friend_name.append(name)

    def add_user_message(self,name,message):
        self.__friend_message[name].append(message)

    def print_username(self):
        for i in self.__friend_name:
            print(i)

    def print_user_message(self,name):
        for i in self.__friend_message[name]:
            print(i)


