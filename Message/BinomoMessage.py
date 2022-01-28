import datetime

from pytz import timezone

from .BaseMessage import Message


class BinomoMessage(Message):
    """Define offer message for Binomo"""

    def create_message(self, offer, addition_text):
        # Calculate time
        date_and_time = datetime.datetime.now(timezone("Europe/Kiev"))
        time_change = datetime.timedelta(minutes=int(offer["time"]))
        time = date_and_time + time_change

        return f"BINOMO - 💰{offer['currency'].upper()} - {time.hour}:{time.minute} {offer['action']}"
