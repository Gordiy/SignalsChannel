import datetime

from pytz import timezone

from .BaseMessage import Message


class BinomoMessage(Message):
    """Define offer message for Binomo"""

    def create_message(self, offer):
        # Calculate time
        date_and_time = datetime.datetime.now(timezone("Europe/Kiev"))
        time_change = datetime.timedelta(minutes=int(offer["time"]))
        time = date_and_time + time_change
        if offer['currency'] == "Взял еще":
            return f"BINOMO - 💰{offer['currency']} до {time.hour}:{time.minute} {offer['action']}, с плечом 2.5."

        return f"BINOMO - 💰{offer['currency'].upper()} - {time.hour}:{time.minute} {offer['action']}"
