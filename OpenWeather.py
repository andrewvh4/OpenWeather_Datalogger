import requests
import json
#import numpy as np
from datetime import *


def getLocation(location):
	with open("Locations.txt", 'r') as f:
		for line in f:
			line = line.replace('\n','')
			line = line.split(',')
			if(line[0]==location):
				return(float(line[1]), float(line[2]))
		print("Error, Location not found:" + location)
		return(0,0)

class OpenWeather():
	APIKey = "NULL"
	
	def init():
		OpenWeather.getAPIKey()
		try:
			open("CallLogs.json", 'r')
		except:
			OpenWeather.makeDataLog()
		
	def getAPIKey():
		global APIKey
		with open("API_KEY.txt", 'r') as f:
			lines = f.readlines()
			APIKey = lines[0].replace('\n', '')
			#print(APIKey)
		return(APIKey)
	def makeDataLog():
		print("Creating New Datalog File")
		with open("CallLogs.json", 'w+') as f:
			data = {}
			data['Entries']=[]
			json.dump(data, f)
			
	def OneCall(lat, lon):	
		r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&appid="+APIKey)
		return(json.loads(r.text))
		
	def storeData(lat, lon, time, data):
		
		with open("CallLogs.json", 'r') as dataLogFile:
			dataLog = json.load(dataLogFile)
	
		dataLog['Entries'].append(data)
			
		with open("CallLogs.json", 'w') as dataLogFile:
			json.dump(dataLog, dataLogFile)
		
		
		'''
		if(data_JSON!={}):
			results = [item for item in data_JSON['results'] if item['datatype']=='TAVG']
		data = []
		for item in results:
			date = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S")
			value = float(item['value'])
			data = data + [[date, value]]
			'''
	
		
	

OpenWeather.init()

lat, lon = getLocation("StL")
OpenWeather.storeData(lat, lon, str(datetime.now()), OpenWeather.OneCall(lat, lon))