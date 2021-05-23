import pyqrcode


def generate_qr(message, filename):
	url = pyqrcode.create(message, encoding='utf-8')
	url.png('resources/generated_qr/%s.png' %filename, scale=4, module_color=[0, 0, 0, 128], 
		background=[0xff, 0xff, 0xcc])
	name = 'code.png'
	path = './' + name 

	return path
