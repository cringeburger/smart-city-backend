from flask import request
from resources.modules import email_sender
from resources import app


@app.post('/send_email')
def send_email():
    reciever_name = request.args['reciever_name']
    mail_domen = request.args['mail_domen']
    subject = request.args['subject']
    filename = request.args['filename']
    
    return email_sender.send(reciever_name, mail_domen, subject, 'kekw', filename)