import requests
import json

header = {
    'Content-Type': 'application/json; charset=utf-8'
}

param = {
    'user': 'reindeer002',
    'mention': 'All of you working very hard!!'
}

response = requests.get('http://34.64.183.225/get', params=param)

print(response.url)