from flask import Flask, render_template, request

from src.core import get_message

app = Flask(__name__)

@app.route("/")
def hello():
#    return render_template('index.html',
#        message=get_message())
    return 'index2'

def run_server():
    app.run(debug=True)

