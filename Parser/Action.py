class Action:
    def __init__(self):
        self.__action = ("ВНИЗ 📉", "ВВЕРХ 📈")
        self.__buy_action = ('buy', "вверх", "верх")
        self.__sell_action = ("sell", "вниз")

    def action(self, text):
        for ac_b in self.__buy_action:
            if ac_b in text:
                return self.__action[0]

        for ac_s in self.__sell_action:
            if ac_s in text:
                return self.__action[1]

        return self.__action
