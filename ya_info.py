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
    return ["5ddec6cf-c3a7-4650-bb09-8e23e3f74f4e","b6a48753-7b36-4868-8a26-54f872aa1135","c486ecba-baab-4d34-81e2-a751280721de","caac70ed-81f7-400b-947d-9ed35897c66e","d66e4886-5a2a-4573-af0a-514f380d96b9"]


