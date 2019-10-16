import spotipy
import pandas as pd
import json


def getTop50(token):
    sp = spotipy.Spotify(auth=token)

    #######Testing
    # results = spotify.search(q='artist:' + 'Kendrick Lamar', type='artist')
    # playlists = sp.user_playlists(username)

    ####### Get US Top 50 ID ##################

    # playlists_US=sp.category_playlists('toplists','US')
    # for i in (playlists_US['playlists']['items']):
    #     if i['name']=='United States Top 50':
    #         print(i['id'])

    ######## END ##############

    top50_playlist = sp.user_playlist_tracks('spotify', '37i9dQZEVXbLRQDuF5jeBp', )
    top50_items = top50_playlist['items']
    res = []
    for song in range(len(top50_playlist['items'])):
        res.append((top50_items[song]['track']['id'], top50_items[song]['track']['name'],
                    top50_items[song]['track']['artists'][0]['name']))
    songID = [x[0] for x in res]
    audio_features = sp.audio_features(songID)
    audio_features = list(filter(None, audio_features))
    print(json.dumps(audio_features,indent=4))
    print(json.dumps(res,indent=4))
    return pd.DataFrame(audio_features)

    # print(json.dumps(a,indent=4))
    # print(json.dumps(res,indent=4))
