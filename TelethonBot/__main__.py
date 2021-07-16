# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

import glob
from pathlib import Path
from TelethonBot.utils import load_plugins
import logging
from . import ATGK


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "TelethonBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("SUCCESSFULLY DEPLOYED!")
print("Enjoy! SPAMMER BOT MADE BY @CRIMINAL786 (MOHAMMAD AMAAN)")

if __name__ == "__main__":
    ATGK.run_until_disconnected()
