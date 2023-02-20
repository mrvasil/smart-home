import requests
import secrets
url = 'https://api.iot.yandex.net/v1.0/devices/caac70ed-81f7-400b-947d-9ed35897c66e'
s = requests.Session()
headers={'Authorization': 'Bearer '+secrets.token}
r=requests.get(url,headers=headers)
print(r.text)

