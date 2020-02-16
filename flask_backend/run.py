
from finalresults import result
from flask import Flask, render_template
import sys
sys.path.append('../')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data=result)


@app.route('/data_page')
def graph():
    return render_template('graphs.html')
