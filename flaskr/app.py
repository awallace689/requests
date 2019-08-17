from flask import Flask, render_template
from flaskr.lib.myrequests.getlib import ResponseWrapper, get
from asyncio import run
from timeit import timeit
from json import dumps

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
@app.route('/home/<url>')
def home(url='https://api.github.com/repos/awallace689/requests/events'):
  start = timeit()
  resp = ResponseWrapper(get(url).json(), debug=False)
  end = timeit()
  print('type', type(resp.source), flush=True)
  print('[time:', end-start, 'sec]', flush=True)
  return render_template(
    'home.html', URL=url, source=resp.source, models=resp.models, is_list=isinstance(resp.source, list))
