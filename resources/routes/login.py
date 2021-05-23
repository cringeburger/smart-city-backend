from flask import request

from resources import app

from resources.db_queries import check_user_login

import json

@app.post('/log_in')
def login_user():
    try:
        data = request.data.decode('utf8')
        return check_user_login(json.loads(data)['login'], json.loads(data)['password'])

    except Exception as e:
        print(e)
