from OpenWeather import *
from time import *
from datetime import *


'''
pyinstaller getHourlyHistory.py --onefile
'''

sec_day = 86400

OpenWeather.init()

try:
	open("HistoryLog.txt", 'r')
except:
	print("Creating new history file")
	with open("HistoryLog.txt", 'w') as f:
		pass

dates = []

with open("HistoryLog.txt", 'r') as f:
	dates=[x.replace('\n', '') for x in f.readlines()]

with open("HistoryLog.txt", 'a') as dateLog:
	with open("Locations.txt", 'r') as locationFile:
		locations = [x.replace('\n', '').split(',') for x in locationFile.readlines()]
		
		for location in locations:
			print("Locations:"+location[0])
		print('\n')
					
		for i in range(6,0,-1):
			timestamp = int(datetime.utcnow().timestamp())-i*sec_day
			if(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d') not in dates):
				print('Date:'+ datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
				dateLog.write('\n'+datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
	
				for location in locations:
					OpenWeather.storeData(OpenWeather.Historical(float(location[1]), float(location[2]), timestamp))
					
sleep(.5)	
