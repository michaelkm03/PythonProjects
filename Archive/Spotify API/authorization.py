import requests
import base64
import six
import urllib

# Construct Auth Header
def _make_authorization_headers(client_id, client_secret):
    auth_header = base64.b64encode(six.text_type(client_id + ':' + client_secret).encode('ascii'))
    return {'Authorization': 'Basic %s' % auth_header.decode('ascii')}

class oAuthObject:

    OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
    OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    access_token = 'BQCyvfsQ2L6K7FlBYwPGDejkqWeaX0UdH8jHc5uWtz3RA66TesDgPN_Aq5i6kRBPaucoQcUJdZqJhP6Ikfo8IQ_5rLyMUNLq16ZNAlBG45k2i02fl-yOzEsuOWKVz608VcgB-E1L5k27D-Q'

    '''
    Creates object to authorize with Spotify API

    Params
       -  client_id
       -  response_type
       -  redirect_uri

    '''

    def __init__(self, client_id, response_type, redirect_uri):
        self.client_id = client_id,
        self.response_type = response_type,
        self.redirect_uri = redirect_uri

    def get_authorize_url(self, state=None):

         payload = {
             'client_id': self.client_id,
             'response_type': self.response_type,
             'redirect_uri': self.redirect_uri
         }

         urlparams = urllib.urlencode(payload)

         return "%s?%s"% (self.OAUTH_AUTHORIZE_URL, urlparams)

a = oAuthObject(client_id='600641ae369b46f590cecf68c5e82014',
                response_type="code",
                redirect_uri='https://open.spotify.com/album/4eLPsYPBmXABThSJ821sqY')

print a.get_authorize_url(state=None)