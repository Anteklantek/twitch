import urllib.request
from urllib.request import Request, urlopen
import json
from Stream import Stream
from pprint import pprint

client_id = '4g8zvm80hxhc3cfp63ipp8fqlj2pad';

req = Request('https://api.twitch.tv/kraken/users?login=anteklantek')
req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
req.add_header('Client-ID', client_id)

resp = urlopen(req)

json_user = json.load(resp)
user_id = json_user['users'][0]['_id']

req = Request('https://api.twitch.tv/kraken/users/' + user_id + '/follows/channels?limit=100')
req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
req.add_header('Client-ID', client_id)

resp = urlopen(req)

json_followed = json.load(resp)
number_total = json_followed['_total']
channels_followed = json_followed['follows']

list_of_ids = []

for i in range(number_total):
    list_of_ids.append(channels_followed[i]['channel']['_id'])

active_url = 'https://api.twitch.tv/kraken/streams/?limit=100&channel='
channels_csv = ','.join(list_of_ids)
active_url += channels_csv


req = Request(active_url)
req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
req.add_header('Client-ID', client_id)

resp = urlopen(req)
json_stream_active = json.load(resp)
number_of_active = json_stream_active['_total']
streams_active = json_stream_active['streams']


list_of_active_streams_deserialized = []


for i in range(number_of_active):
    json_stream_active_i = streams_active[i]
    name = json_stream_active_i['channel']['name']
    status = json_stream_active_i['channel']['status']
    game = json_stream_active_i['channel']['game']
    viewers = json_stream_active_i['viewers']
    list_of_active_streams_deserialized.append(str(Stream(name, status, viewers, game)))



for stream in list_of_active_streams_deserialized:
    print(stream)