import requests

daily = ['spotify:playlist:37i9dQZF1E36fSwXIhiYTS','spotify:playlist:37i9dQZF1E35kMPHR2eNVl','spotify:playlist:37i9dQZF1E39vkG45qETcn','spotify:playlist:37i9dQZF1E35ZIs08CeQyQ','spotify:playlist:37i9dQZF1E34RelE7aOor2','spotify:playlist:37i9dQZF1E34YhwlCe9Hd0'];
headers = {}
liked_songs = open('Daily-Mix/liked-songs', 'r')
disliked_songs = open('Daily-Mix/disliked-songs', 'r')
final_list = []
playlits = []

def pull_mix(mix_link):
    pull = requests.get('https://api.spotify.com/v1/playlists/${a}/tracks'.format(mix_link), headers=headers)
    print(pull.status_code, pull.reason)
    mix = pull.json()['items']
    return mix


def filter(mix, list):
    fmix = []
    for s in mix:
        if(s in list):
            continue
        else:
            fmix.append(s)
    
    return fmix



#for id in daily:
print(pull_mix(daily[0]))




