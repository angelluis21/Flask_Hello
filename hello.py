from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_word():
    return 'Hola, mundo'
    