import lucia.ui, glob, os
m=[]
i=0
def load():
	menu = lucia.ui.Menu()
	for file in glob.glob("tracks/*.map"):
		menu.add_item_tts(os.path.basename(file).split('.')[0],file)
	menu.add_item_tts("return","q")
	result = menu.run("please choose a track")
	if result=="q":return 2
	global i
	i=0
	global m
	m=open(result,"r").read().split("\n")
	return 0
def next():
	global i
	i+=2
	try:
		return (int(m[i-2]), m[i-1])
	except:
		return (0,"")

def meen(val):
	match val:
		case "jump":return "jump over"
		case "pit":return "pit"
		case "trick":return "trick jump"
		case "ft":return "finish turn"
		case _:
				if val[0]=="r":return "right turn"
				if val[0]=="l":return "left turn"
	return val
