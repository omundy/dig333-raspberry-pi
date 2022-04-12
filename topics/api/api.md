← [Raspberry Pi](../../README.md)

<a href="../../README.md"><img width="150" src="../../assets/img/RPi-Logo-Reg-SCREEN.webp"></a>

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

Weather.gov documentation
https://weather-gov.github.io/api/general-faqs
