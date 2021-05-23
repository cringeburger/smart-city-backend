from resources import app
from resources.routes import (login, profile, send_qr, send_mail, user_balance, registration, organizations)
from flask import request


# @app.after_request
# def add_cors_headers(response):
# 	try:
# 		if '26.237.70.37' in request.referrer:
# 			response.headers.add('Access-Control-Allow-Origin', '*')
# 			response.headers.add('Access-Control-Allow-Credentials', 'true')
# 			response.headers.add('Access-Control-Allow-Headers', '*')
# 			response.headers.add('Access-Control-Allow-Headers', '*')
# 			response.headers.add('Access-Control-Allow-Headers', '*')
# 			response.headers.add('Access-Control-Allow-Headers', '*')
# 			response.headers.add('Access-Control-Allow-Methods', '*')
# 	except Exception as e:
# 		print(e)

# 	return response


@app.route('/')
def main():
	return '<h2 align="middle">Smart city api v0.0.1</h2>'
	