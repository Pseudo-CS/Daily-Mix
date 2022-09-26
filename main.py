import base64
import requests

client_id = 'eda12a570bbc45acb1838434b482f684'
client_secret = '0cb0b76eb9594ebcac2f507f01b139d9'
final = client_id + ':' + client_secret
final = str(base64.b64encode(bytes(final, 'utf-8'))).strip('b\'').strip('\'')


headers = {'Authorization': 'Basic ' + final, 
            'Content-Type': 'application/x-www-form-urlencoded'}
data = {'grant_type': 'client_credentials'}


daily = ['37i9dQZF1E36fSwXIhiYTS','spotify:playlist:37i9dQZF1E35kMPHR2eNVl','spotify:playlist:37i9dQZF1E39vkG45qETcn','spotify:playlist:37i9dQZF1E35ZIs08CeQyQ','spotify:playlist:37i9dQZF1E34RelE7aOor2','spotify:playlist:37i9dQZF1E34YhwlCe9Hd0'];
liked_songs = open('Daily-Mix/liked-songs', 'r')
disliked_songs = open('Daily-Mix/disliked-songs', 'r')
final_list = []
playlist = ['2VqgmD4YcRG9wrgSD4xuMs']


def pull_mix(mix_link):
    try:
        r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    except:
        print(r.status_code, r.reason)

    headin = {'Authorization': 'Bearer ' + r.json().get('access_token')}

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

    try:
        r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    except:
        print(r.status_code, r.reason)

    headin = {'Authorization': 'Bearer ' + r.json().get('access_token')}

    for ur in flist:
        try:
            pull = requests.post('https://api.spotify.com/v1/playlists/{mix}/tracks?uris={uri}'.format(mix=mix, uri=ur['track']['uri']), headers=headin)
        except:
            print(pull.status_code, pull.reason)



dg = pull_mix(daily[0])
last = filter(dg, liked_songs)
update(playlist[0], last)


#testing the update function




