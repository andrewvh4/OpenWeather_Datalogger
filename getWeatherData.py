from OpenWeather import *
import time

OpenWeather.init()

with open("Locations.txt", 'r') as f:
	for line in f:
		line = line.replace('\n','')
		line = line.split(',')
		print("Gathering Data:"+line[0])
		OpenWeather.storeData(OpenWeather.OneCall(float(line[1]), float(line[2])))
	time.sleep(1)	
		
