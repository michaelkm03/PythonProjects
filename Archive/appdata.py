import urllib2
import urllib
import json

# Construct URL
app_id = raw_input('Enter app id here:  ')
s_param = 'lookup'
url = 'http://itunes.apple.com/'+s_param+'?'+'id='+app_id
print url

# Read response, parse as JSON
response = urllib2.urlopen(url)

# data = response.read()
json_obj = json.load(response)

for i in json_obj['results']:
   print ''
   print '----- CONFIG -----'
   print ''
   print 'AppStore Name:           ',i['trackCensoredName']
   print 'Developer Account:       ',i['sellerName']
   print 'Original Launch Date:    ',i['releaseDate']
   print 'Languages:               ',i['languageCodesISO2A'][0]
   print 'File Size:               ',i['fileSizeBytes']
   print 'Min Req. iOS:            ',i['minimumOsVersion']
   print 'Currency:                ',i['currency']
   print 'Price:                   ',i['price']
   print 'Is Game Center Enabled:  ',i['isGameCenterEnabled']
   print ''
   print '----- METADATA -----'
   print ''
   print 'LIVE Version:                  ',i['version']
   print 'Current Version Release Date:  ',i['currentVersionReleaseDate']
   print 'Primary Category:              ',i['genres'][0]
   print 'Secondary Category:            ',i['genres'][1]
   print 'Content Rating:                ',i['contentAdvisoryRating']
   print 'Company ID:                    ',i['artistId']
   print 'Bundle ID:                     ',i['bundleId']
#   print 'Average User Rating:           ',i['averageUserRating']
#   print 'User Rating Count:             ',i['userRatingCount']
   print ''
   print '----- ASSETS -----'
   print 'App Icon'
   print '(x60):        ',i['artworkUrl60']
   print '(x100)        ',i['artworkUrl100']
   print '(x512)        ',i['artworkUrl512']
   print ''
   print '----- SCREENSHOTS -----'
   print ''
   print 'Image #1     ',i['screenshotUrls'][0]
   print 'Image #2     ',i['screenshotUrls'][1]
   print 'Image #3     ',i['screenshotUrls'][2]
   print 'Image #4     ',i['screenshotUrls'][3]
   print ''
   print '---------- STORE DESCRIPTION ----------'
   print ' '
   print i['description']
   print ' '
   print '---------- RELEASE NOTES ----------'
   print ' '
   print i['releaseNotes']
   print ' '
   print ' '
   print '----------------------------------------'
   print ''
   print ''
   print '################################################'
   print 'CURRENTLY LIVE WITH:  ',i['version']
   print '################################################'
   print ''
   print ''
