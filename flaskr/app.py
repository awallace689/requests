from flask import Flask, render_template
from flaskr.lib.myrequests.getlib import get_json, ResponseWrapper

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
@app.route('/home/<url>')
def home(url='https://api.github.com/repos/awallace689/requests/events'):
  return render_template('home.html', URL=url)
