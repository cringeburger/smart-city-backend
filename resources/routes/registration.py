from resources import app


@app.post('/sign_in')
def reg_user():
    return 'success'
