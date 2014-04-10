import scraper
from suffix_dict import dino_dict
import random
from start import db
#from db_model_postgres import db  # will it run the script?


class Link(db.Model):
  dino_link = db.Column(db.String(200), primary_key = True)
  website = db.Column(db.String(200))

  def __init__(self, website, dino_link):
    self.website = website
    self.dino_link

  def set_link(website, dino_link):
    new_link = Link(website, dino_link)
    db.session.add(link)
    db.session.commit()

  def get_link(short_link):
    return Link.query.filter_by(dino_link = short_link).first()



def make_tiny(url, hostname):
  # keep going until it's not in the dictionary of shortened links
    print "in make tiny: " + url + '\n'
    key = new_dino_name(url)
    #print db_model.get_url(key)
    while db_model.get_link(key) != None:
      key = new_dino_name(url)
    db.set_link(url, key)
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
  return db_model.get_link(key)
  #if key in key_dict:
   ## url = key_dict[key]
   # return url
 # else:
   # return ''
