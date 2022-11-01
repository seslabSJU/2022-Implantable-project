import requests
import json

header = {
    'Content-Type': 'application/json; charset=utf-8'
}

body = {
    'user': 'reindeer002',
    'mention': 'All of you working very hard!!'
}

response = requests.post('http://34.64.183.225/post', json=body, headers=header)

print(response.text)