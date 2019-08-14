from flask import Flask, render_template
from flaskr.lib.myrequests.getlib import get_json, ResponseWrapper
from asyncio import run
from timeit import timeit
from json import dumps

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
@app.route('/home/<url>')
def home(url='https://api.github.com/repos/awallace689/requests/events'):
  start = timeit()
  resp = ResponseWrapper(get_json(url), debug=True)
  end = timeit()
  print('[time:', end-start, 'sec]', flush=True)
  return render_template(
  #  'home.html')
    'home.html', URL=url, source=resp.source, models=resp.models)
