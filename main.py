#https://accounts.spotify.com/authorize?client_id=eda12a570bbc45acb1838434b482f684&response_type=code&redirect_uri=http://localhost:8000&scope=playlist-modify-public+playlist-modify-private 

import base64
import requests

client_id = 'eda12a570bbc45acb1838434b482f684'
client_secret = '0cb0b76eb9594ebcac2f507f01b139d9'
final = client_id + ':' + client_secret
final = str(base64.b64encode(bytes(final, 'utf-8'))).strip('b\'').strip('\'')


headers = {'Authorization': 'Basic ' + final, 
            'Content-Type': 'application/x-www-form-urlencoded'}
data = {'grant_type': 'authorization_code',
        'code': 'AQC3aBuMIyMk9_LPxTf5EWLS-3N5NTwg3vk5sFnk_V9x3dP7T3shoBGL1i00jkLOLz2K0YwRy_YozqlK5-FHCVu0XvV3kirB19VKxnhtiP1XtyoSZxoTBWj0f6UG20EZC1TPS4kZRgyr4bKwhuNZ3WeT1ZhCp-V9vn2nbsZw6XGDhJb_YkpunO2D-7Ave9bkDdCnLrFIqN0rHA1CJzpZagKPbt8ZRGNAqng',
        'redirect_uri': 'http://localhost:8000'}


daily = ['37i9dQZF1E36fSwXIhiYTS','spotify:playlist:37i9dQZF1E35kMPHR2eNVl','spotify:playlist:37i9dQZF1E39vkG45qETcn','spotify:playlist:37i9dQZF1E35ZIs08CeQyQ','spotify:playlist:37i9dQZF1E34RelE7aOor2','spotify:playlist:37i9dQZF1E34YhwlCe9Hd0'];
liked_songs = open('Daily-Mix/liked-songs', 'r')
disliked_songs = open('Daily-Mix/disliked-songs', 'r')
final_list = []
playlist = ['2VqgmD4YcRG9wrgSD4xuMs']



def access_token():
    r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    print(r.status_code, r.reason)
    if(r.status_code==200): return r
    

acc = access_token().json().get('access_token')
headin = {'Authorization': 'Bearer ' + acc}

#BQAUx-db-wYLr-HQlJPN0yxtXElo6v8VVp8UAyRmRRjJC4isL3UxUDHTGEgIG9eKs3KT4h08vLj7w9V8xifxZYnh2CgWexZycJ2kxtSJJiitQdx21VgileK7gLkojdwjyCsiPnFnviyn_C0js6MOmU7LwZW6B4DNujUqZRLE0-JmYndIprOahDBoDAyh6xh_wCIkzH-McCgtH--gscarfizmxR4T5rhKvdWZpLrgnQeV6OyFzRmTK48DyLQcPzc
#AQBmH68mYqJdsuAleUpn93FeyqH6nKcdgJpmVzwtnLH7SnfKq0_WIFoDafvZVVfM-mpuXTjTkjkT8QDsRA9PHXSYWYHyxaCqs2jxPoR5gIsWq6b4cVAUVHGk7erQ0kD1-lQ


def pull_mix(mix_link):

    pull = requests.get('https://api.spotify.com/v1/playlists/{m}/tracks'.format(m=mix_link), headers=headin)
    print(pull.status_code, pull.reason)
    mix = pull.json()['items']
    return mix


def filter(mix, list):
    fmix = []
    file = list.read()
    for s in mix:
        if(s['track']['name'] in file):
            continue
        else:
            fmix.append(s)
    
    return fmix


def update(mix, flist):

    for ur in flist:
        try:
            pull = requests.post('https://api.spotify.com/v1/playlists/{mix}/tracks?uris={uri}'.format(mix=mix, uri=ur['track']['uri']), headers=headin)
        except:
            print(pull.status_code, pull.reason)



dg = pull_mix(daily[0])
last = filter(dg, liked_songs)
update(playlist[0], last)


#testing the update function




