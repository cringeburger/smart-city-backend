from resources import app

from flask import request


@app.post('/sign_in')
def reg_user():
    try:
        data = request.data.decode('utf8')
        # return check_user_login(json.loads(data)['login'], json.loads(data)['password'])
        return 1
    except Exception as e:
        print(e)
