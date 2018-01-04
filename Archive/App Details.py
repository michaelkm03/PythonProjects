import vams_common as vams
import requests
import sys

_DEFAULT_HOST = 'https://api.getvictorious.com'
app_details_endpoint = '/api/app/apps_list'


def fetchAppDetails(server):

    # Calculate request hash
    url = '%s%s' % (_DEFAULT_HOST, app_details_endpoint)

    date = vams.createDateString()

    req_hash = vams.calcAuthHash(app_details_endpoint, 'GET', date)

    auth_header = 'BASIC %s:%s' % (vams._DEFAULT_VAMS_USERID, req_hash)

    headers = {
        'Authorization': auth_header,
        'User-Agent': vams._DEFAULT_USERAGENT,
        'Date': date
    }

    response = requests.get(url, headers=headers)
    print response.text
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
        fetchAppDetails(server)
    else:
        print 'There was a problem authenticating with the Victorious backend. Exiting now...'
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)