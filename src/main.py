from funcs import *
import sounds
from sounds import dic as son
import time
import map
import lucia.utils
import sys
sys.path.append("../..")
import lucia
lucia.initialize(audiobackend=lucia.AudioBackend.BASS)
sounds.load()

mainmenu()

sounds.destroy()
lucia.quit()
