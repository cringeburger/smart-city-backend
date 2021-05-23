from flask import request, send_file

from resources import app

from resources.modules.qr_generator import generate_qr

from datetime import date


@app.get('/send_qr')
def send_qr():
	user_token = request.args['user_token']
	# mail_domen = request.args['mail_domen']
	# subject = request.args['subject']
	filename = 'qr_'+str(date.today()) + '_' + user_token

	generate_qr('https://www.youtube.com/watch?v=dQw4w9WgXcQ', filename)

	return send_file('generated_qr\\' + filename+ '.png', mimetype='image/png')