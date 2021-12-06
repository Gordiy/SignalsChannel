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
            offer_act = self._action.action(text)
            self._action = offer_act

        if self.__currency and self.__time and self._action:
            return {
                "time": self.__time,
                "currency": self.__currency.replace(" ", ''),
                "action": self._action
            }