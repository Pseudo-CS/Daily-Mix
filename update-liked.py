import requests

headin = {'Authorization': 'Bearer BQD-UjLjxZ-y4yC3GeP2SWELCWsQ15LdG_D5HCjXdfY_QAtybX9fQgSE3y66uU0i7kCjeiYJ9PVaU4V_WjMHOURcUHbqgoNavT29J0YJsCJ3TjfVrxog2UN5Rd4lJiKIfv0o7yHRyQjjikyx8JszU_mNy_TBTrisuzb4NMQ8QNkofurDOUXqVqvUM8ZgG2_StcDoVnYHZng_'}

liked_songs = open('Daily-Mix/liked-songs', 'a')

d = requests.get('https://api.spotify.com/v1/me/tracks?limit=20&offset=0', headers=headin)
print(d.status_code, d.reason)
    

for i in d.json()['items']:
    liked_songs.write('\n' + i['track']['name'] + ' - ' + i['track']['artists'][0]['name'])
    
liked_songs.close()