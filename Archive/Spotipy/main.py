import spotipy
import client as c
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json
import requests

client_credentials_manager = SpotifyClientCredentials(client_id='600641ae369b46f590cecf68c5e82014', client_secret='e714aaaa22ae4867a88f4ddb17a3b925')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
user_id = '1278539789'
user = sp.user(user_id)

trace = False  # Enable tracing?
trace_out = False
max_get_retries = 10

def QuerySpotifyForTrack (search_term, limit, type):
    if limit > 50:
        print '%s is above the limit or not an integer, please select an integer below 50...\n\n' % limit
    else:
        type = type
        print '\n############## Search Results (%s Max) ################\n\n' % limit
        search = sp.search(search_term, limit=limit, offset=0, type=type)
        if type == 'playlist':
            print 'type is playlist...'
        else:
            track_results = search['tracks']
            c = 0
        for i in track_results['items']:
            album_name = i['album']['name']
            album_url = i['album']['external_urls']
            artist_name = i['artists'][0]['name']
            artist_id = i['artists'][0]['id']
            track_name = i['name']
            track_preview = i['preview_url']
            cover_art = i['album']['images'][0]['url']
            print "[",(c + 1),"]","\nARTIST:     %s" \
                              "\nALBUM:      %s" \
                              "\nTRACK:      %s" \
                              "\nPREVIEW:    %s" \
                              "\nCOVER:      %s\n\n" % (artist_name, album_name, track_name,track_preview, cover_art)
            c += 1

# QuerySpotifyForTrack('king kunta',10,'trasudo pip install --upgrade google-api-python-clientck')
# QuerySpotifyForTrack(sys.argv[1], sys.argv[2], sys.argv[3])

def GetCurrentUserPlaylistInfo():
    playlists = sp.user_playlists(user_id, limit=50, offset=0)
    while playlists:
        print '\n##### Playlists Created by %s #####\n' %  user['display_name']
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s >>> %s" % (i + 1 , playlist['name'], playlist['id']))
            track = sp._get("users/%s/playlists/%s/tracks" % (user_id, playlist['id']),limit=50)
            items = track['items']
            for dic in items:
                print dic
            playlists = sp.next(playlists)
        else:
            playlists = None

r = sp.featured_playlists()
print r
class JSON_Object:
     def __init__(self, response, name):
         self.response = r
         self.name = name

#x = JSON_Object(r, 'Michael')
#print x.name


# for items in obj['playlists']:
#     for i in items:
#         for j in i[0]:
#             print j
