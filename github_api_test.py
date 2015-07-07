import json, requests

url = 'https://github.com/repos/pilla/try_git/hooks'

params = ''

resp = requests.get(url=url)
# data = json.loads(resp.text)

print (resp.text)
# print (data)

