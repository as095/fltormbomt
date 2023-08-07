# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "9590156"))
	API_HASH = os.environ.get("API_HASH", "368a346bb1b206b650f2b3b37f91e237")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6397316252:AAG7OB8AhWkrBF7mahykbLKDS0BXF4G7_Cc")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Animex_Shows_Hubbot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001695047717"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "6180541080"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://altair:altair@cluster0.iuwgcxr.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001978359564")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001695047717")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "0").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = f"""
This bot is to get links of anime files. To get files link you need to join updates channel below 👇🏻

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

🧑🏻‍💻 **Developer:** @Pampa_Jee

📢 **Updates Channel:** [Animex Shows Hub](https://t.me/Animex_shows)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Pampa_Jee

I Make Telegram Bots At Cheap Price 
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
