from resources import app
from resources.routes import login

@app.route('/')
def main():
    return '<h2 align="middle">Smart city api v0.0.1</h2>'
    