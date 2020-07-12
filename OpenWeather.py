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
			open("HourlyHistory.json", 'r')
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
		with open("HourlyHistory.json", 'w+') as f:
			data = {}
			json.dump(data, f)
			
	def Historical(lat, lon, time):
		r = requests.get("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+str(lat)+"&lon="+str(lon)+"&dt="+str(time)+"&exclude=current&appid="+APIKey)
		return(json.loads(r.text))
	
	def OneCall(lat, lon):	
		r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&appid="+APIKey)
		return(json.loads(r.text))
		
	def storeData(data):
		with open("HourlyHistory.json", 'r') as dataLogFile:
			dataLog = json.load(dataLogFile)

		location=str(data["lat"])+'/'+str(data["lon"])
		
		if(location not in dataLog):
			dataLog[location]={}
			dataLog[location]["lat"]=data["lat"]
			dataLog[location]["lon"]=data["lon"]
			dataLog[location]["timezone"]=data["timezone"]
			dataLog[location]["timezone_offset"]=data["timezone_offset"]
			dataLog[location]['hourly']=[]
			
		dataLog[location]['hourly']=dataLog[location]['hourly']+data['hourly']
			
		with open("HourlyHistory.json", 'w') as dataLogFile:
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