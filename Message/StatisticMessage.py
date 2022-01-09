from .BaseMessage import Message


class StatisticMessage(Message):
    """ Define statistic message"""
    def create_message(self, text, additional_text):
        return f"{text} {additional_text}"
        