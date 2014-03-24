import scraper
from suffix_dict import dino_dict
import random

key_dict = {}

def make_tiny(url, hostname):
  # keep going until it's not in the dictionary of shortened links

    print "in make tiny: " + url
    global key_dict
    key = new_dino_name(url)
    while key in key_dict.keys():
      key = new_dino_name(url)
    key_dict[key] = url
    return ('%s/%s') %(hostname, key)


def get_dino_suffix():
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
  suffix = get_dino_suffix()
  prefix = scraper.get_a_word(url)
  return prefix + suffix




def get_url(key):
  if key in key_dict:
    url = key_dict[key]
    return url
  else:
    return ''
