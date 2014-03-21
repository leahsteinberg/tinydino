from flask import Flask
from flask import render_template
from flask import request, redirect
import random

app = Flask(__name__)

key_dict = {}
di_path = 'dinosaurs'
dinosaurs = None
def make_tiny(url, hostname):
    global key_dict

    key = get_random_unqiue_dinosaur()
    key_dict[key] = url
    
    return ('%s/%s') %(hostname, key)

def load_dinosaurs():
    global di_path
    global dinosaurs   

    dinosaurs = []
    f = open(di_path, 'r')
    for line in f:
        dinosaurs.append(line.strip())

 
def get_random_unqiue_dinosaur():
    global dinosaurs   
    
    if dinosaurs is None:
        load_dinosaurs()

    l = len(dinosaurs)
    r = random.randint(0, l-1)
    
    while dinosaurs[r] in key_dict:
        print r, dinosaurs[r], len(key_dict)
        r = random.randint(0, l-1)

    return dinosaurs[r]        


@app.route('/<key>')
def redir_Url(key):
    #redir
    global key_dict
    print key, key_dict
    if key in key_dict:
        url = key_dict[key]
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