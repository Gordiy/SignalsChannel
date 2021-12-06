from .Action import Action


class BaseParser:
    def __init__(self):
        self.__time = None
        self.__currency = None
        self._action = Action()

    def parse_message(self, text):
        pass
