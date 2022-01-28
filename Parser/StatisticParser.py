from .BaseParser import BaseParser


class StatisticParser(BaseParser):
    def __goodwill_statistic(self, text):
        words = ("❌", "✅")
        if words[0] in text:
            return False
        else:
            return True

    def __smart_trader_statistic(self, text):
        words = ("плюс", "минус")
        if words[0] in text:
            return True
        elif words[1]:
            return False
        else:
            return None

    def parse_message(self, text, trader):
        if trader == "smart_trader":
            return self.__smart_trader_statistic(text)
        else:
            return self.__goodwill_statistic(text)
