import requests
open('yandex.json', 'w').close()
url = 'https://api.iot.yandex.net/v1.0/user/info'
s = requests.Session()
headers={'Authorization': 'Bearer y0_AgAAAAAnPIZcAAkRogAAAADcNmS0FoHWvTPASH2wWGsjDLWQGKTKBTo'}
r=requests.get(url,headers=headers)
print(r.text)
open('yandex.json', 'a').write(r.text)
