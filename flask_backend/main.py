from finalresults import result
from flask import Flask, render_template
import sys
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data=result)


@app.route('/data_page')
def graph():
    return render_template('graphs.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
