from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template('index.html')

@app.route('/about')
def hello_about():
    return render_template('about.html')

@app.route('/post')
def hello_post():
    return render_template('post.html')

@app.route('/contact')
def hello_contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()