import requests
import secrets
def info1():
    if len(secrets.token) < 6:
        import start
        start.start()
        return 0
    url = 'https://api.iot.yandex.net/v1.0/user/info'
    s = requests.Session()
    headers={'Authorization': 'Bearer '+secrets.token}
    r=requests.get(url,headers=headers)
    return r.text


