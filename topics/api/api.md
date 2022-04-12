
# APIs



## Simple example

```python
from requests import get
import json

# davidson
url = 'https://api.weather.gov/gridpoints/GSP/116,76/forecast/hourly'
# the first index inside properties is the current weather
temp = get(url).json()['properties']['periods'][0]['temperature']
# print with text
print("Current temperature in Davidson: " + str(temp) + " F")
```
