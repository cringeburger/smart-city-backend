from flask import request

from resources import app

from resources.db_queries.user_profile_inf import get_user_inf
from resources.db_queries.all_achievements import all_achs

import json


@app.post('/profile')
def profile():
	try:
		token = json.loads(request.data.decode('utf8'))['token'].replace(' token=', '')
		return get_user_inf(token)
	
	except Exception as e:
		print(e)


@app.post('/allachivements')
def all_ach():
	try:
		token = json.loads(request.data.decode('utf8'))['token'].replace(' token=', '')
		return all_achs(token)
	
	except Exception as e:
		print(e)
