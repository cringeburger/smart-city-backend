from flask import request

from resources import app


@app.route('/log_in', method=['POST', 'OPTIONS'])
def login_user():
    data = request.data
    print(data)
    return 'success'
