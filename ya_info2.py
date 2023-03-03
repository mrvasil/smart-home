import requests
import json

token=str(open("secrets.txt").readlines()[-1])
sp = []
url = 'https://api.iot.yandex.net/v1.0/user/info'
s = requests.Session()
headers={'Authorization': 'Bearer '+token}
r=requests.get(url,headers=headers)
js=json.loads(r.text)
devices, state_sp = [], []
sp_info, sp_name = [], []
dev=js['devices']
for i in range(len(dev)):
    devices.append(dev[i].get('id'))
    sp_name.append(dev[i].get('name'))
    sp_info.append(dev[i].get('type'))
    if (sp_info[-1] == 'devices.types.light'):
        state_sp.append(dev[i].get("capabilities")[2].get("state").get("value"))
    if  (sp_info[-1] == 'devices.types.socket'):
        state_sp.append(dev[i].get("capabilities")[0].get("state").get("value"))
print(devices)
print(sp_name)
print(sp_info)
print(state_sp)