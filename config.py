# ============================================================
#Group Manager Bot
# Author: Zerox (https://github.com/itszerox_official) 
# Support: https://t.me/VoidRealm_Official
# Channel: https://t.me/Knull_Reaml
# YouTube: https://youtube.com/@its-zerox-official
# License: Open-source (keep credits, no resale)
# ============================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("OWNER_ID", 0))
BOT_USERNAME = os.getenv("BOT_USERNAME", "GhoulxHelpBot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/VoidRealm_Official")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/Knull_Realm")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/jhfdfq.jpg")
