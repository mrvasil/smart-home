import requests
import json
def info1():
    token=str(open("secrets.txt").readlines()[-1])
    if len(token) < 6:
        import start
        start.start()
        return 0
    dict={}
    url = 'https://api.iot.yandex.net/v1.0/user/info'
    s = requests.Session()
    headers={'Authorization': 'Bearer '+token}
    r=requests.get(url,headers=headers)
    js=json.loads(r.text)
##
    dict['devices'], dict['state'] = [], []
    dict['info'], dict['name'] = [], []
    dev=js['devices']
    for i in range(len(dev)):
        dict['devices'].append(dev[i].get('id'))
        dict['name'].append(dev[i].get('name'))
        dict['info'].append(dev[i].get('type'))
        if (dict['info'][-1] == 'devices.types.light'):
            dict['state'].append(dev[i].get("capabilities")[2].get("state").get("value"))
        if  (dict['info'][-1] == 'devices.types.socket'):
            dict['state'].append(dev[i].get("capabilities")[0].get("state").get("value"))


##
    scenarios1=js["scenarios"]
    id, name, dict['scenarios'] = [], [], []
    for i in range(0, len(scenarios1), 1):
        id.append(scenarios1[i].get('id', 0))
        name.append(scenarios1[i].get('name', 0))
    dict['scenarios'].append(id)
    dict['scenarios'].append(name)

    dict['token']=token

    return dict
