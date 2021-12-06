import re

from .BaseParser import BaseParser


class GoodwillParser(BaseParser):
    def parse_message(self, text):
        stop = ("❌", "✅")
        if stop[0] not in text or stop[1] not in text:
            self.__currency = re.findall(r"\b\w{3} / \w{3}\b", text)
            self.__time = 5
            offer_act = self.__action.action(text)
            self.__action = offer_act
