import requests

token = ''
headin = {'Authorization': 'Bearer '+token}

liked_songs = open('Daily-Mix/liked-songs', 'r+')

d = requests.get('https://api.spotify.com/v1/me/tracks?limit=5&offset=0', headers=headin)
print(d.status_code, d.reason)
    
myfile = liked_songs.read()

for i in d.json()['items']:
    entry = i['track']['name'] + ' - ' + i['track']['artists'][0]['name']

    if(entry in myfile):
        break
    else:
        liked_songs.write('\n' + entry)

liked_songs.close()
