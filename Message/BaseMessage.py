class Message:
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message
