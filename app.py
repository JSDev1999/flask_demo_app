from flask import Flask, render_template, url_for
import requests

url = "https://bing-news-search1.p.rapidapi.com/news"

querystring = {"safeSearch":"Off","textFormat":"Raw"}

headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Key": "63d28da5bemsh5cf54013327a228p1cb755jsn23338e042adb",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
}

responsedata = requests.request("GET", url, headers=headers, params=querystring)
finalData = responsedata.text
print(finalData)
name='ramesh'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template('index.html', posts=responsedata.text , name=name)
    #return response.text

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
    app.run(debug=True)