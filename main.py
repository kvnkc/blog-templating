from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/post')
def posts():
    url = 'https://api.npoint.io/4af156202f984d3464c3'
    response = requests.get(url=url)
    post_data = response.json()
    return render_template('post.html', posts=post_data)


if __name__ == "__main__":
    app.run(debug=True)
