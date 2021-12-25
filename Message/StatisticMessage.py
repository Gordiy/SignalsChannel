from .BaseMessage import BaseMessage


class StatisticMessage(BaseMessage):
    """ Define statistic message"""
    def create_message(self, text, additional_text):
        return f"{text} {additional_text}"
        