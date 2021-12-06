from .BaseMessage import Message


class PocketOptionMessage(Message):
    def create_message(self, offer, addition_text):
        return f"{offer['currency'].upper()} - {offer['time']} мин. {offer['action']} \n \n {addition_text}"
