from flask import *
from requests import post
import sys
from urllib.parse import urlencode
import secrets

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

client_id = secrets.client_id
client_secret = secrets.client_secret
baseurl = 'https://oauth.yandex.ru/'
app = Flask(__name__)
text = """<h1 style="margin: 100;width: 1100px;" class="text-justify">Отлично, Вы авторизованны<br>Теперь нажмите "Я авторизовался" и откройте прилоежение заново.</h1>"""


dict1={}

@app.route('/')
def index():
    global dict1
    if request.args.get('code', False):
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': client_id,
            'client_secret': client_secret
        }
        data = urlencode(data)
        token = post(baseurl + "token", data).json().get('access_token')
        if len(str(token)) > 6:
            dict1[request.cookies.get('secret_code')] = str(token)
            print(dict1)
        return text
    else:
        secret_code = request.args.get("secret")
        dict1[secret_code] = ''
        res1 = make_response(redirect(baseurl + "authorize?response_type=code&client_id={}".format(client_id)))
        res1.set_cookie('secret_code',secret_code)
        return res1
    
@app.route('/token')
def token():
    global dict1
    return dict1[str(request.args.get("secret"))]

def authorization():
    app.run(host='0.0.0.0', port=8912)

authorization()