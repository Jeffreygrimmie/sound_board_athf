#Jeffrey Grimmie 3/8/2019
#aqua teen hunger force sound board

import os
from pygame import mixer

def build_lst(lst):
	track = 0 #start track number
	for index in lst: #build list of tracks and sound files avalible
		print('Track: {} = {}'.format(track, index))
		track += 1 #increase track by 1 for eack pass through the loop
def clear(): #clears the console
	os.system('cls' if os.name == 'nt' else 'clear')

lst = os.listdir("sounds") #list all sounds in the sounds directory

mixer.init() # initialize pygame mixer

while True: #main loop
	try:
		clear() #clear the console
		build_lst(lst) #build the list of tracks
		inpt = input("\nPlease select a track by entering it's\ncorresponding number or enter 'q' to quit: ") #get user input
		if inpt == "q": #check for user input of q
			break #end program if user input q
		else: # play user selected track
			mixer.music.load("sounds\\%s" % lst[int(inpt)]) #load track
			mixer.music.play() #play track
	except Exception: #if user input is not a valid track or a q continue
		continue #continue