from flask import Flask, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)


## login
@app.route('/')
@app.route('/<name>')
def index(name=None):
    error = None
    return render_template("index.html", name=name)

@app.route('/shoping')
def shopping():
    food=["chiness","chsss","kdjdjjd","kskskskksk"]
    ##return render_template("shoping.html",food=food)
    return jsonify("food",food[1],food[2])

if __name__ == '__main__':
    app.debug = True
    app.run()