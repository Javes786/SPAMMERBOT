# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

import sys
import logging
import importlib
from telethon import TelegramClient, events
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"TelethonBot/plugins/{plugin_name}.py")
    name = "TelethonBot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["TelethonBot.plugins." + plugin_name] = load
    print("SPAMMER BOT has IMPoRTED " + plugin_name)
