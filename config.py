import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN  = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID   = int(os.getenv("OWNER_ID", "5712520691"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1003025900916"))  # ← leído del .env
OFFICIAL_WEB = "https://telegramp2p.pro"
AGENT_USER   = "@CriptoJay"
