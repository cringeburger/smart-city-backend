import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

# Custom
from resources.modules.config import email_val, password


def send(reciever_name, mail_domen, subject, msg_text, file_name=None):

	message = MIMEMultipart('alternative')
	message.set_charset('utf8')

	# Sender email
	message['FROM'] = email_val

	# Reciever email
	reciever_mail = reciever_name + '@' + mail_domen
	message['To'] = reciever_mail

	# Mail subject
	message['Subject'] = Header(subject, 'utf-8')
	_attach = MIMEText(msg_text.encode('utf-8'), 'html', 'UTF-8')
	message.attach(_attach)

	if file_name != None:
		try:
			with open(file_name, 'rb') as attachment:
				img = MIMEImage(attachment.read())
				img.add_header('Content-Disposition', 'attachment', filename='qr.png')
				message.attach(img)
		except Exception as e:
			print(e)
	

	with smtplib.SMTP('smtp.gmail.com: 587') as server:
		server.starttls()
		server.login(email_val, password)
		server.sendmail(email_val, reciever_mail, message.as_string())

	return 'success'

# print(send('vbcfgfgf@mail.ru', 'kek!', 'Важное сообщение', './code.png'))
