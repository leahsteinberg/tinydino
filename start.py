from flask import Flask
from flask import render_template
from flask import request, redirect
import random, requests, dinologic
from flask.ext.sqlalchemy import SQLAlchemy #~~~~
import os

app = Flask(__name__)
#app._static_folder = "../bootstrap/css/bootstrap.min.css"
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] #~~~~
db = SQLAlchemy(app)


@app.route('/<key>')
def redir_Url(key):
    #redir
    # calls something in dinologic to get the full url, then goes to that website
    url = dinologic.get_url(key)
    if url is not '':
      return redirect('http://' + url, code = 302)
    else:
        return 'Error: id does not exist'

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print '1111'
    if request.method == 'POST':
        print "222222"
        url = request.form['linkbox']
        print "3333333 "
        tiny_url = dinologic.make_tiny(url, request.host)
        return render_template('redir.html', long_url = 'http://'+url, tiny_url = tiny_url)
    else:
        print "444"
        print request
        print "555"
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
    
