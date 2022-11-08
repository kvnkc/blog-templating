from flask import Flask, render_template
import requests

url = 'https://api.npoint.io/4af156202f984d3464c3'
response = requests.get(url=url)
post_data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_data)


@app.route('/post/<int:post_id>')
def posts(post_id):
    for post in post_data:
        if post_id == post['id']:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
