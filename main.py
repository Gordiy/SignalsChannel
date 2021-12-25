import config
from Message.BinomoMessage import BinomoMessage
from Message.PocketOptionMessage import PocketOptionMessage
from Parser.GoodwillParser import GoodwillParser
from Parser.SmartTraderParser import SmartTraderParser
from telethon import TelegramClient, events

client = TelegramClient(config.SESSION, config.TG_APP_ID, config.TG_APP_SECRET)


async def get_entity(ent):
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.name == ent:
            entity = ent
            return entity


def get_additional_text(additional_file_name):
    with open(f"{config.STATIC_FOLDER}/{additional_file_name}", "r") as file:
        return file.read()


@client.on(
    events.NewMessage(
        chats=config.TG_READ_MSG_CHAT,
        pattern=r"(?i).*{}".format(config.TRADER_PATTERNS["goodwill"]),
    )
)
async def goodwill_handler(event):
    entity = await get_entity(config.TG_SEND_MSG_CHAT)

    if entity:
        offer = GoodwillParser().parse_message(event.message.text.lower())
        if offer:
            add_text = get_additional_text("additional_text.txt")
            our_message_pocket = PocketOptionMessage(None).create_message(
                offer, add_text
            )
            our_message_binomo = BinomoMessage(None).create_message(offer, add_text)
            await client.send_message(entity=entity, message=our_message_pocket)
            await client.send_message(entity=entity, message=our_message_binomo)


@client.on(events.NewMessage(chats=config.TG_READ_MSG_CHAT))
async def smart_handler(event):
    if config.TRADER_PATTERNS["smart_trader"] in event.message.text:
        entity = await get_entity(config.TG_SEND_MSG_CHAT)

        if not entity:
            return

        offer = SmartTraderParser().parse_message(event.message.text.lower())
        if offer and int(offer["time"]) <= 5:
            add_text = get_additional_text("additional_text.txt")
            our_message_pocket = PocketOptionMessage(None).create_message(
                offer, add_text
            )
            our_message_binomo = BinomoMessage(None).create_message(offer, add_text)
            await client.send_message(entity=entity, message=our_message_pocket)
            await client.send_message(entity=entity, message=our_message_binomo)
        else:
            pass


client.start()
client.run_until_disconnected()
