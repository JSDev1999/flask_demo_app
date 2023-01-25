from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def hello_about():
    return 'Hello World! from about page!!'

if __name__ == '__main__':
    app.run()