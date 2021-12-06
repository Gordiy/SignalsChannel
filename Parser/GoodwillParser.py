import re

from .BaseParser import BaseParser


class GoodwillParser(BaseParser):
    def parse_message(self, text):
        stop = ("❌", "✅")
        action = ("BUY", "SELL")
        if stop[0] not in text or stop[1] not in text:
            self.__currency = re.findall(r"\b\w{3}/\w{3}\b", text)
            self.__time = 5
            if action[0] in text:
                self.__action = None
