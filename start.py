from flask import Flask
from flask import render_template
from flask import request, redirect
import random, requests
from flask.ext.sqlalchemy import SQLAlchemy #~~~~
from suffix_dict import dino_dict
import scraper
import random
import os

app = Flask(__name__)
#app._static_folder = "../bootstrap/css/bootstrap.min.css"
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db') #~~~~
db = SQLAlchemy(app)
#db.create_all()


@app.route('/<key>')
def redir_Url(key):
    #redir
    # calls something in dinologic to get the full url, then goes to that website
    url = get_url(key)
    if url is not '':
      return redirect('http://' + url, code = 302)
    else:
        return 'Error: id does not exist'

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        url = request.form['linkbox']
        print "url is " + url
        tiny_url = make_tiny(url, request.host)
        print "tiny url ~~~", tiny_url
	return render_template('redir.html', long_url = 'http://'+url, tiny_url = tiny_url)
    else:

        return render_template('index.html')




class Link(db.Model):
  dino_link = db.Column(db.String(200), primary_key = True)
  website = db.Column(db.String(200))

  def __init__(self, website, dino_link):
    self.website = website
    self.dino_link = dino_link




def make_tiny(url, hostname):
  # keep going until it's not in the dictionary of shortened links
    print "in make tiny: " + url + '\n'
    key = new_dino_name(url)
    print "in make tiny: " + key + '\n'
    #print db_model.get_url(key)
    #while key not in Link.query.all():
    #while Link.query.filter_by(dino_link = key).first() != None:
      #key = new_dino_name(url)
    new_link = Link(url, key)
    db.session.add(new_link)
    db.session.commit()
    return ('%s/%s') %(hostname, key)


def get_dino_suffix():
  print 'in get dino suffix\n'
  accum = 0.0
  rand_num = random.random()
  for key in dino_dict.keys():
    accum+=dino_dict[key]
    if rand_num < accum:
      return key
  else:
    print "UH OH!"

def new_dino_name(url):
  # pick dino suffix
  # get word from url
  # concatenate
  print 'in new dino name\n'
  suffix = get_dino_suffix()
  prefix = scraper.get_a_word(url)
  return prefix + suffix




def get_url(key):
  return Link.query.filter_by(dino_link = key).first()
  #if key in key_dict:
   ## url = key_dict[key]
   # return url
 # else:
   # return ''

if __name__ == '__main__':
    app.run(debug = True)
    
