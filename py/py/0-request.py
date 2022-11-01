import requests
import json

header = {
    'Content-Type': 'application/json; charset=utf-8'
}

response = requests.get('http://34.64.183.225', headers=header)
print(response.text)
print(response.request.url)