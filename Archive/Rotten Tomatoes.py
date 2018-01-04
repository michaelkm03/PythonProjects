import requests
import urllib
import Stopipy

url = 'https://www.rottentomatoes.com/search/?search=the accountant'
request = requests.get(url)
data = urllib.urlopen(url)

for i in data:
    print i
