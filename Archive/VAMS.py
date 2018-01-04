import vams_common as vams
import requests
import sys
import json

_DEFAULT_HOST = 'https://api.getvictorious.com'
_APPLIST_ENDPOINT = '/api/app/app_by_build_name'

def fetchAppList(server):
    """Retrieves the list of ACTIVE (Locked or Unlocked) apps from VAMS.

    Returns:
        List of app info on active apps.
    """

    # Calculate request hash
    url = '%s%s' % (_DEFAULT_HOST, _APPLIST_ENDPOINT )
    print url
    date = vams.createDateString()

    req_hash = vams.calcAuthHash(_APPLIST_ENDPOINT , 'GET', date)
    print req_hash

    auth_header = 'BASIC %s:%s' % (vams._DEFAULT_VAMS_USERID, req_hash)

    headers = {
        'Authorization': auth_header,
        'User-Agent': vams._DEFAULT_USERAGENT,
        'Date': date
    }
    response = requests.get(url, headers=headers)
    json_obj = json.loads(response.text)
    print json_obj
    # for i in json_obj['payload']:
    #     print '========================================================'
    #     print 'App ID:            ', i['app_id']
    #     print 'App Name:          ', i['app_name']
    #     print 'Build Name:        ', i['build_name']
    #     print 'Google Play ID:    ', i['google_play_id']
    #     print 'Apple ID:          ', i['apple_id']
    #     print 'Android Icon:      ', i['icon_android']
    #     print 'iOS Icon:          ', i['icon_ios']
    #     print '========================================================'
    #



def main(argv):

    vams.init()

    if len(argv) == 1:
        server = 'production'
    else:
        if argv[1] == 'h' or argv[1] == 'help':
            print '...so...looking for help?'
        else:
            server = argv[1]

    global _DEFAULT_HOST
    _DEFAULT_HOST = vams.GetVictoriousHost(server)

    if vams.authenticateUser(_DEFAULT_HOST):
        fetchAppList(server)
    else:
        print 'There was a problem authenticating with the Victorious backend. Exiting now...'
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)