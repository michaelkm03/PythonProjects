import requests
import vams_common as vams

_APPLIST_ENDPOINT = '/api/app/apps_list'
vams_id = vams.init()

def fetchAppList(server):
    """Retrieves the list of ACTIVE (Locked or Unlocked) apps from VAMS.

    Returns:
        List of app info on active apps.
    """
    # dictionary of Victorious_App_ID [Apple_ID]
    d = {}
    # Calculate request hash
    url = '%s%s' % ('https://api.getvictorious.com', _APPLIST_ENDPOINT)
    date = vams.createDateString()
    req_hash = vams.calcAuthHash(_APPLIST_ENDPOINT, 'GET', date)

    auth_header = 'BASIC %s:%s' % (vams._DEFAULT_VAMS_USERID, req_hash)

    headers = {
        'Authorization': auth_header,
        'User-Agent': vams._DEFAULT_USERAGENT,
        'Date': date
    }
    response = requests.get(url, headers=headers)
    json_obj = response.json()
    error_code = json_obj['error']

    if error_code == 0:
        app_count = 0
    payload = json_obj['payload']
    for i in payload:
        APPLE_ID = i['apple_id']
        # APP_NAME = i['app_name']
        build_name = i['build_name']
        d.update({build_name: APPLE_ID})

fetchAppList('production')