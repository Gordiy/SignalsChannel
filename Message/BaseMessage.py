class Message:
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message

    def create_message(self, offer, addition_text):
        pass
