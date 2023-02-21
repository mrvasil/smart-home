import requests
import secrets
import json
def info1():
    if len(secrets.token) < 6:
        import start
        start.start()
        return 0
    
    #url = 'https://api.iot.yandex.net/v1.0/user/info'
    #s = requests.Session()
    #headers={'Authorization': 'Bearer '+secrets.token}
    #r=requests.get(url,headers=headers)
    #
    #devices, dev=json.loads(r.text).get('rooms', 0), []
    #for i in range(0, len(devices), 1):
    #    dev.append(devices[i]["devices"])
    #devices = sum(dev, [])
    #
    #sp_info, sp_name = [], []
    #for i in range(len(devices)):
    #    s = requests.Session()
    #    url = 'https://api.iot.yandex.net/v1.0/devices/'+str(devices[i])
    #    headers={'Authorization': 'Bearer '+secrets.token}
    #    r=requests.get(url,headers=headers)
    #    sp_info.append(json.loads(r.text).get('type', 0))
    #    sp_name.append(json.loads(r.text).get('name', 0))
    #sp=[]
    #sp.append(sp_info)
    #sp.append(sp_name)

    sp=[]
    sp.append(['devices.types.light', 'devices.types.socket', 'devices.types.smart_speaker.yandex.station.mini_2', 'devices.types.light', 'devices.types.light', 'devices.types.light'])
    sp.append(['Лампочка', 'Розетка', 'Станция Мини', 'Лампочка', 'Лампочка', 'Лампочка'])
    return sp


