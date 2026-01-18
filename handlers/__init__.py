# ============================================================
# Group Manager Bot
# Author: Zerox (https://github.com/itszerox_official)
# Support: https://t.me/VoidRealm_Official
# Channel: https://t.me/Knull_Reaml
# YouTube: https://youtube.com/@its-zerox-official
# License: Open-source (keep credits, no resale)
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    print("✅ Group commands registered!")

