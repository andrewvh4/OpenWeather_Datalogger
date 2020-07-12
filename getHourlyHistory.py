from OpenWeather import *
import time
import datetime


'''
pyinstaller getHourlyHistory.py --onefile
'''

sec_day = 86400

OpenWeather.init()

days=-1

while True:
	print("Days to Look Back:", end = '')
	days = int(input())
	if (days > 5):
		print("Cannot go farther than 5 days")
	elif (days<0):
		print("Days must be positive")
	else:
		print("")
		break

with open("Locations.txt", 'r') as f:
	for line in f:
		line = line.replace('\n','')
		line = line.split(',')
		print("Gathering Data:"+line[0])
		for i in range(1, days+1):
			timestamp = int(datetime.datetime.utcnow().timestamp())-i*sec_day
			print('\tDate:'+ datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
			OpenWeather.storeData(OpenWeather.Historical(float(line[1]), float(line[2]), timestamp))
	time.sleep(.5)	

