import lucia
import os.path	
import glob
dic={}
def load():
	global dic
	for file in glob.glob("sounds/*.*"):
		f=os.path.basename(file).split('.')[0]
		dic[f]=lucia.audio_backend.sound.Sound()
		dic[f].load(file)
def destroy():
	global dic
	for a, b in dic.items():
		try:
			b.close()
		except:
			pass

def crash():
	global dic
	dic["fall"].play_wait()