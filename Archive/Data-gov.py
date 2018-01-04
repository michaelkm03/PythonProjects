import urllib, urllib2
import json

# HTTP request and add response to JSON Object
response = urllib2.urlopen('https://demo.ckan.org/api/3/action/package_list')
assert response.code == 200
response_dict = json.loads(response.read())
if response_dict['success'] is True:
    for i in response_dict['result']:
        print i
        result = response_dict['result']
else:
    print '...Something went wrong'

print result