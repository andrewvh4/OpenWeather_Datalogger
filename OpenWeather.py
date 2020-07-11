import requests
import json
#import numpy as np
from datetime import *

APIKey = "NULL"

def getAPIKey():
	global APIKey
	with open("API_KEY.txt", 'r') as f:
		lines = f.readlines()
		APIKey = lines[0].replace('\n', '')
		print(APIKey)
	return(APIKey)

def getLocation(location):
	with open("Locations.txt", 'r') as f:
		for line in f:
			line = line.replace('\n','')
			line = line.split(',')
			if(line[0]==location):
				return(float(line[1]), float(line[2]))
		print("Error, Location not found:" + location)
		return(0,0)

def OneCall(lat, lon):
	global APIKey
	r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid="+APIKey)
	print(r.text)
	data_JSON = json.loads(r.text)
	results = []
	'''
	if(data_JSON!={}):
		results = [item for item in data_JSON['results'] if item['datatype']=='TAVG']
	data = []
	for item in results:
		date = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S")
		value = float(item['value'])
		data = data + [[date, value]]
		'''
	#return(data)
	
	
getAPIKey()
print(getLocation("StL"))
print(APIKey)