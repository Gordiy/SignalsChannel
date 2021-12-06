import re
from .BaseParser import BaseParser


class SmartTraderParser(BaseParser):
    """
    Message parser for Smart Trader (Трейдер с умом) trading signals.
    """
    def parse_message(self, text):
        stop = ('через',)
        if stop[0] not in text:
            currency = re.findall(r'\b\w{3}/\w{3}\b', text)
            if not currency:
                currency = re.findall(r'\b\w{3} \w{3}\b', text)

            try:
                self.__currency = currency[0]
            except KeyError:
                # if currency not found, exit from function
                return

            minutes = ""
            for i in range(len(text)):
                if text[i].isdigit():
                    minutes += text[i]

            if minutes != "":
                self.__time = int(minutes[0:2])

            offer_act = self._action.action(text)
            self._action = offer_act

        if self.__currency and self.__time and self._action:
            return {
                "time": self.__time,
                "currency": self.__currency,
                "action": self._action
            }
