from flask import Flask, request, jsonify, redirect
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
text = """<h1 style="margin: 0 auto;width: 1100px;" class="text-justify">Отлично, Вы авторизованны<br>Теперь закройте окно приложения и зайдите заново.</h1>"""

@app.route('/')
def index():
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
            f = open("secrets.py", 'a').write("""\ntoken='"""+str(token)+"""'""")
            

        return text#jsonify(post(baseurl + "token", data).json())
    else:
        return redirect(baseurl + "authorize?response_type=code&client_id={}".format(client_id))


def authorization():
    app.run(host='127.0.0.1', port=8912)
    exit()