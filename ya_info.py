import requests
import secrets
import json
def info1():
    if len(secrets.token) < 6:
        import start
        start.start()
        return 0
    url = 'https://api.iot.yandex.net/v1.0/user/info'
    s = requests.Session()
    headers={'Authorization': 'Bearer '+secrets.token}
    r=requests.get(url,headers=headers)

    #devices = ["5ddec6cf-c3a7-4650-bb09-8e23e3f74f4e","b6a48753-7b36-4868-8a26-54f872aa1135","c486ecba-baab-4d34-81e2-a751280721de","caac70ed-81f7-400b-947d-9ed35897c66e","d66e4886-5a2a-4573-af0a-514f380d96b9"]
    #sp_info = []
    #sp_name = []
    #for i in range(len(devices)):
    #    s = requests.Session()
    #    url = 'https://api.iot.yandex.net/v1.0/devices/'+devices[i]
    #    headers={'Authorization': 'Bearer '+secrets.token}
    #    r=requests.get(url,headers=headers)
    #    sp_info.append(json.loads(r.text).get('type', 0))
    #    sp_name.append(json.loads(r.text).get('name', 0))
    #sp=[]
    #sp.append(sp_info)
    #sp.append(sp_name)

    sp=[]
    sp.append(['devices.types.light', 'devices.types.smart_speaker.yandex.station.mini_2', 'devices.types.light', 'devices.types.light', 'devices.types.light'])
    sp.append(['Лампочка', 'Станция Мини', 'Лампочка', 'Лампочка', 'Лампочка'])
    return sp
info1()


