from .Action import Action


class BaseParser:
    def __init__(self):
        self.__time = None
        self.__currency = None
        self.__action = Action()

        self.__offer = {}

    def parse_message(self, text):
        pass

    @property
    def time(self):
        return self.time

    @property
    def offer(self):
        return self.__offer
