from flask import request
from flask_cors import cross_origin

from resources import app

from resources.db_queries.user_balance_add import upd_balance, user_balance

import json


@app.post('/update_balance')
def add_balance():
	try:
		token = json.loads(request.data.decode('utf8'))['token'].replace(' token=', '')
		balance = json.loads(request.data.decode('utf8'))['balance']
		upd_balance(token, balance)
		
		return 'success'

	except Exception as e:
		print(e)


@app.post('/user_balance')
def show_balance():
	try:
		token = json.loads(request.data.decode('utf8'))['token'].replace(' token=', '')
		return user_balance(token)
	
	except Exception as e:
		print(e)