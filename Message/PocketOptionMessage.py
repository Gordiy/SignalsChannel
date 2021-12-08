from .BaseMessage import Message


class PocketOptionMessage(Message):
    """Define offer message for Pocket Option"""
    def create_message(self, offer, addition_text):
        return f"Pocket Option \n💰{offer['currency'].upper()} - {offer['time']} мин. {offer['action']} \n \n{addition_text}"
