from flask import request

from resources import app

from resources.db_queries.organizations import org_inf, org_list

import json


@app.post('/organization')
def organization():
	try:
		org_id = json.loads(request.data.decode('utf8'))['link']
		return org_inf(org_id)
	
	except Exception as e:
		print(e)


@app.route('/organizations', methods=['GET', 'POST'])	
def organizations():
	try:
		org_tp = json.loads(request.data.decode('utf8'))['token']
		return org_list(org_tp)
	
	except Exception as e:
		print(e)
