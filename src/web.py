from flask import Flask, render_template, request

from src.core import get_message

from data import Articles

app = Flask(__name__)

#Articles = Articles()

@app.route("/")
def hello():
#    return render_template('home.html',
#        message=get_message())
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')#, articles = Articles)

#def run_server():
#    app.run(debug=True)

if __name__ == '__main__': 
     app.run(debug=True)
