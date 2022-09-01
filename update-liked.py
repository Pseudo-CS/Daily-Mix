import requests

token = 'BQCuIF4u-B2khNnAEqsf4zRqdITZ0zCblzDBNpgESr8kK-wUG6WdBkbmUsdJ0vZzvxoBZI_4NxnoEp3ychVFgMMqyMtc4l7_KbHr4xJyYshBczxx2ynzIr3FyxZywKc6-8Ij5dKoaPnGDrVcKBRTasivlg2maAhSwcM4uvh6Ox3T7yw8xqXofl35a3CyoYaH-gDQpJSArLoR'
headin = {'Authorization': 'Bearer '+token}

# liked_songs = open('Daily-Mix/liked-songs', 'a')
liked_songs = open('Daily-Mix/liked-songs', 'a+')

d = requests.get('https://api.spotify.com/v1/me/tracks?limit=5&offset=0', headers=headin)
print(d.status_code, d.reason)
    

for i in d.json()['items']:
    entry = i['track']['name'] + ' - ' + i['track']['artists'][0]['name']
    if(entry in liked_songs.read()):
        break
    liked_songs.write('\n' + entry)

liked_songs.close()
