from requests import get
import json
from pprint import pprint



# 1. Find the lat,lng for a location
# https://www.latlong.net/
location = "Davidson"
lat = 35.4993
lng = -80.8487

# 2. Plug those into the api url to find the gridpoint
# https://api.weather.gov/points/35.4993,-80.8487

gridX = 116
gridY = 76

# 3. Look for the forecast url in ^
# https://api.weather.gov/gridpoints/GSP/116,76/forecast

def weather_data_from_api():
	# concate the grid X,Y to get hourly forecast
    url = 'https://api.weather.gov/gridpoints/GSP/' + str(gridX) + ',' + str(gridY) + '/forecast/hourly'
	# return only properties
    return get(url).json()['properties']


# 4. Get the current weather from the periods property

def current_weather():
	# get data
    data = weather_data_from_api()
	# get list of periods
    periods = list(data['periods'])
	# first has current
    return periods[0]


current = current_weather()
print ("Current temperature: " + str(current['temperature']) + " F")
