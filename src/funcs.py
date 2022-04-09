import sounds
from sounds import dic as son
import time
import map
import lucia.utils
import lucia
version="1.0"
ex=True
speed=1.0
speedstep=0.01
alt=0
x=0
y=0
turning=0
jumping=False
turntimer=lucia.utils.timer.Timer()
jump=lucia.utils.timer.Timer()
timer=lucia.utils.timer.Timer()
ya=0
yb=""
window="adventure on the snow"
btimer=lucia.utils.timer.Timer()




def mainmenu():
	resetvars()
	for it, val in son.items():
		try:
			val.stop()
		except:
			pass

	test = lucia.show_window(window)
	menu = lucia.ui.Menu()
	menu.add_item_tts("Start game","s")
	menu.add_item_tts("test speakers","t")
	menu.add_item_tts("exit","q")
	result = menu.run(window+", version "+version+". please choose an option")
	match result:
		case "s":
			res=gameloop()
			if res==1:return mainmenu()
			if res==2:
				crash()
				return mainmenu()

		case "q":
			return

def getready():
	for i in range(10,0,-1):
		if lucia.key_pressed(lucia.K_q):return 1
		lucia.output.braille(str(i))
		if i<=3:son["beep"].play()
		while timer.elapsed<1000:
			time.sleep(0.005)
		timer.restart()
	son["racestart"].play()
	son["racestart2"].play()
	return 0
def ahead():
	yr=yb.split(" ")
	match yr[0]:
		case "jump":
			son["speshel1"].play()
		case "end":
			son["combodone"].play()
		case "l":
			son["locked"].pan=-100
			son["locked"].play()
		case "r":
			son["locked"].pan=100
			son["locked"].play()
		case "down":
			if float(yr[1])>0.02:son["boost"].play()



	lucia.output.speak(map.meen(yb)+" ahead!")


def gameloop():
	global ex
	if ex:
		theload=map.load()
		if theload==2:return mainmenu()
		lucia.output.speak("you are now up on a big hill. your skees are fixed with a rope. and they will release your skees in a few seconds. get ready.")
	jump.pause()
	son["amb"].play_looped()
	ready=getready()
	if ready==1:ex=false
	timer.restart()
	son["sliding"].play_looped()
	btimer.restart()
	global speed, x, y, ya, yb, jumping, turning, alt,speedstep
	while ex:
		lucia.process_events()
		if turning!=0 and turntimer.elapsed>=(1000/abs(turning)):
			turntimer.restart()
			if turning>0 and x>-20:x-=1
			if turning<0 and x<20:x+=1
			son["sliding"].pan=x*5

		if btimer.elapsed>=100:
			if lucia.key_down(lucia.K_RIGHT) and x<20:
				x+=1
				son["sliding"].pan=x*5
			if lucia.key_down(lucia.K_LEFT) and x>-20:
				x-=1
				son["sliding"].pan=x*5
			if lucia.key_down(lucia.K_BACKSPACE):
				if speed>1.0:speed-=0.05
				son["sliding2"].play()
			else:son["sliding2"].stop()

			if lucia.key_down(lucia.K_SPACE):
				jumping=True
				jump.restart()
				son["sliding"].stop()
				son["jump"].play()
			if jumping and jump.elapsed>=1000:
				son["land"].play()
				son["sliding"].play_looped()
				jump.pause()
				jumping=False

			lucia.output.braille(str(x)+"  "+str(y)+"  "+str(ya)+"  "+map.meen(yb))
			btimer.restart()
		if timer.elapsed>=1000/speed:
			if not lucia.key_down(lucia.K_BACKSPACE):speed+=speedstep
			timer.restart()
			y+=1
			ya-=1
			if ya==10:ahead()
			if ya<=5 and yb!="ft" and yb!="end":
				if yb[0]=="l":
					son["flag"].pan=-100
				elif yb[0]=="r":
					son["flag"].pan=100
				else:
					son["flag"].pan=0

				son["flag"].stop()
				son["flag"].play()


		if ya<=0:
			yc=yb.split(" ")
			match yc[0]:
				case "jump":
					if not jumping:
						sounds.crash()
						return 1
					else:
						son["trickboost"].play()
				case "r":
					turning=int(yc[1])
					son["trickloop"].pan=100
					son["trickloop"].play()
				case "l":
					turning=-int(yc[1])
					son["trickloop"].pan=-100
					son["trickloop"].play()
				case "ft":
					turning=0
					son["trickloop"].pan=0
					son["trickloop"].play()
				case "up":speedstep=-float(yc[1])
				case "down":speedstep=float(yc[1])


			ya,yb=map.next()
			if ya>0 and ya<10:ahead()

		if ya==0:
			son["sliding"].stop()
			son["win"].play_wait()
			return 1

		if lucia.key_pressed(lucia.K_q):
			return 1
		time.sleep(0.005)
def resetvars():
	for it, val in sounds.dic.items():
		try:
			val.stop()
		except:
			pass
	global speed, x, y, ya, yb, jumping, turning, alt,speedstep
	speed=1.0
	speedstep=0.01
	alt=0
	x=0
	y=0
	turning=0
	jumping=False
	ya=0
	yb=""