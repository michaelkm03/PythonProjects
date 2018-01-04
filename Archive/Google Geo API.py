import urllib
import json
from math import sin, cos, sqrt, atan2, radians

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address_1 = raw_input('Enter first location:  ')
address_2 = raw_input('Enter second location:  ')

url_1 = serviceurl + urllib.urlencode({'sensor':'false','address':address_1})
url_2 = serviceurl + urllib.urlencode({'sensor':'false','address':address_2})
print 'Retrieving first city',url_1
print 'Retrieving second city',url_2

site_1 = urllib.urlopen(url_1)
site_2 = urllib.urlopen(url_2)
data_1 = site_1.read()
data_2 = site_2.read()
js_1 = json.loads(str(data_1))
js_2 = json.loads(str(data_2))


# Results form user input 1
lat_1 = js_1['results'][0]['geometry']['location']['lat']
lng_1= js_1['results'][0]['geometry']['location']['lng']
city_name_1 = js_1['results'][0]['address_components'][0]['long_name']
state_1 = js_1['results'][0]['address_components'][2]['long_name']
country_1 = js_1['results'][0]['address_components'][3]['long_name']

# Results form user input 2
lat_2 = js_2['results'][0]['geometry']['location']['lat']
lng_2= js_2['results'][0]['geometry']['location']['lng']
city_name_2 = js_2['results'][0]['address_components'][0]['long_name']
state_2 = js_2['results'][0]['address_components'][2]['long_name']
country_2 = js_2['results'][0]['address_components'][3]['long_name']


# approximate radius of earth in km
R = 6373.0

lat1 = radians(lat_1)
lon1 = radians(lng_1)
lat2 = radians(lat_2)
lon2 = radians(lng_2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print ''
print '---------- City 1 ----------'
print ''
print 'City:  ',city_name_1
print 'State:  ',state_1
print 'Country:  ',country_1
print 'Latitude: ',lat_1
print 'Longitude: ',lng_1
print ''
print '---------- City 2 ----------'
print 'City:  ',city_name_2
print 'State:  ',state_2
print 'Country:  ',country_2
print 'Latitude: ',lat_2
print 'Longitude: ',lng_2
# print json.dumps(js_1,indent=4)
# print json.dumps(js_2,indent=4)
print ''
print '---------- DISTANCE ----------'
print ''
print 'Distance between the two cities is', distance,'km'




