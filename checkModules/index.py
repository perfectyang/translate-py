from flask import Flask, render_template
from version import startCheck
import os
curpath = os.path.dirname(os.getcwd())
print(curpath)
lists = startCheck(os.path.join(curpath, 'node_modules'))
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('node.html', list=lists)
app.run(debug=True, port=5000)