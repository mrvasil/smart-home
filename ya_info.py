import requests
import json
def info1():
    token=str(open("secrets.txt").readlines()[-1])
    if len(token) < 6:
        import start
        start.start()
        return 0
    sp = []
    url = 'https://api.iot.yandex.net/v1.0/user/info'
    s = requests.Session()
    headers={'Authorization': 'Bearer '+token}
    r=requests.get(url,headers=headers)
    js=json.loads(r.text)
##
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


##
    scenarios1=js["scenarios"]
    id, name, scenarios = [], [], []
    for i in range(0, len(scenarios1), 1):
        id.append(scenarios1[i].get('id', 0))
        name.append(scenarios1[i].get('name', 0))
    scenarios.append(id)
    scenarios.append(name)
##
    sp.append(sp_info)
    sp.append(sp_name)
    sp.append(devices)
    sp.append(scenarios)
    sp.append(token)
    sp.append(state_sp)
    return sp