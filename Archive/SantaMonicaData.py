import requests
import json

PARKING_LOTS_URL = "https://data.smgov.net/resource/tce2-7ir6.json"
POLICE_CALLS_FOR_SERVICE_URL = 'https://data.smgov.net/resource/xx64-wi4x.json'

response = requests.get(POLICE_CALLS_FOR_SERVICE_URL)
json_data = json.loads(response.text)
for i in json_data:
    print i