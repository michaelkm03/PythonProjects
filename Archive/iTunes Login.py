import urllib2
import json

# Construct URL, user enters Apple app id for desired LIVE app
app_id = raw_input('Enter app id here:  ')
x = 'lookup'
url = 'http://itunes.apple.com/'+x+'?'+'id='+app_id

# Read response from URL post, store in JSON object
response = urllib2.urlopen(url)
json_obj = json.load(response)

# Parse JSON object
for i in json_obj['results']:
    
    print '----- ASSETS -----'
    print 'App Icon'
    print '     (x60):  ',i['artworkUrl60']
    print '     (x100)', i['artworkUrl100']
    print '     (x512)', i['artworkUrl512']
    print 'Screenshots:  ',i['screenshotUrls']
    print ''
    print '----- CONFIG -----'
    print ''
    print 'Developer Account:  ',i['sellerName']
    print 'Original Launch Date:  ',i['releaseDate']
    print 'Languages:  ',i['languageCodesISO2A']
    print 'File Size:  ',i['fileSizeBytes']
    print 'Min Req. iOS:  ',i['minimumOsVersion']
    print 'Currency:  ',i['currency']
    print 'Price:  ',i['price']
    print 'Is Game Center Enabled:  ',i['isGameCenterEnabled']
    print ''
    print '----- METADATA -----'
    print ''
    print 'AppStore Name:   ',i['trackCensoredName']
    print 'LIVE Version:  ',i['version']
    print 'Current Version Release Date:  ',i['currentVersionReleaseDate']
    print 'Categories:  ',i['genres']
    print 'Content Rating:  ',i['contentAdvisoryRating']
    print 'Company ID:  ',i['artistId']
    print 'Bundle ID:  ',i['bundleId']
    print 'Average User Rating:  ',i['averageUserRating']
    print 'User Rating Count:  ',i['userRatingCount']
    print ''
    print '---------- STORE DESCRIPTION ----------'
    print ' '
    print i['description']
    print ' '
    print ' '
    print '---------- RELEASE NOTES ----------'
    print ' '
    print i['releaseNotes']



