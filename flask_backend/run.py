
from flask import Flask, render_template
import sys
sys.path.append('../')
app = Flask(__name__)

from finalresults import result

@app.route('/')
def hello_world():
    return render_template('index.html', data=result)
