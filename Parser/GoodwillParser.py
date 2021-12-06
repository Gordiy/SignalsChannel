import re

from .BaseParser import BaseParser


class GoodwillParser(BaseParser):
    """
    Message parser for Goodwill Bot M5 trading signals.
    """
    def parse_message(self, text):
        stop = ("❌", "✅")
        if stop[0] not in text or stop[1] not in text:
            self.__currency = re.findall(r"\b\w{3} / \w{3}\b", text)[0]
            self.__time = 5
            offer_act = self.__action.action(text)
            self.__action = offer_act
