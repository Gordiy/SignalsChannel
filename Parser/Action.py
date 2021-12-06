class Action:
    def __init__(self, text):
        self._text = text
        self.__action = ("вниз", "вверх")
        self.__buy_action = ('buy', "вверх", "верх")
        self.__sell_action = ("sell", "вниз")

    @property
    def action(self):
        for ac_b in self.__buy_action:
            if ac_b in self._text:
                return self.__action[0]

        for ac_s in self.__sell_action:
            if ac_s in self._text:
                return self.__action[1]

        return self.__action
