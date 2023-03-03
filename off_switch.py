import keyboard
import requests
from threading import Thread
a = '68aab3ac-e0b6-4386-9b11-82c76535f5ca'
token = 'y0_AgAAAAAnPIZcAAkRogAAAADdc12gbj_9iUP5SOaK4nbYPbCBE350HDc'
def a1():
    while True:
        keyboard.wait("Alt+q")
        url = 'https://api.iot.yandex.net/v1.0/devices/actions'
        s = requests.Session()
        headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
        data1 = '''{"devices": [{"id": "'''+a+'''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": false}}]}]}'''
        r=requests.post(url,headers=headers,data=data1)
def a2():
    while True:
        keyboard.wait("Alt+w")
        url = 'https://api.iot.yandex.net/v1.0/devices/actions'
        s = requests.Session()
        headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
        data1 = '''{"devices": [{"id": "'''+a+'''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": true}}]}]}'''
        r=requests.post(url,headers=headers,data=data1)
def a3():
    while True:
        keyboard.wait("Alt+й")
        url = 'https://api.iot.yandex.net/v1.0/devices/actions'
        s = requests.Session()
        headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
        data1 = '''{"devices": [{"id": "'''+a+'''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": false}}]}]}'''
        r=requests.post(url,headers=headers,data=data1)
def a4():
    while True:
        keyboard.wait("Alt+ц")
        url = 'https://api.iot.yandex.net/v1.0/devices/actions'
        s = requests.Session()
        headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
        data1 = '''{"devices": [{"id": "'''+a+'''","actions": [{"type": "devices.capabilities.on_off","state": {"instance": "on","value": true}}]}]}'''
        r=requests.post(url,headers=headers,data=data1)

t1 = Thread(target=a1, args=())
t2 = Thread(target=a2, args=())
t3 = Thread(target=a3, args=())
t4 = Thread(target=a4, args=())

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()