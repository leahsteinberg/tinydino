from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

dict = {}
key = 0
def make_tiny(url, hostname):
    global dict
    global key

    key += 1
    dict[key] = url
    
    return ('%s/%s') %(hostname, key)

@app.route('/<int:key>')
def redir_Url(key):
    #redir
    global dict

    if key in dict:
        url = dict[key]
        return redirect('http://' + url, code = 302)
    else:
        return 'Error: id does not exsist'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        url = request.form['linkbox']
        tiny_url = make_tiny(url, request.host)
        return render_template('redir.html', long_url = 'http://'+url, tiny_url = tiny_url)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)