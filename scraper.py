import requests
from bs4 import BeautifulSoup
import sys
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords

def get_dinosaurs():
    di_list = []
    html = requests.get('http://en.wikipedia.org/wiki/List_of_dinosaurs').content
    
    soup = BeautifulSoup(html)
    possible_names = soup.findAll('i')
    for name in possible_names:
        a = name.find('a')
        if a is not None:
            if name.text not in di_list:
                di_list.append(name.text)

    return di_list

def save_list(list, filepath):
    f = open(filepath, 'w')
    for l in list:
        if l.strip() != '':
            f.write(l + '\n')  
    f.close()

def get_a_word(url):
    print "in get a word: " + url
    if url[:7] is not "http://":
      url = 'http://'+ url
    try:
      html = requests.get(url)
    except requests.ConnectionError, e:
        return 'dino'
        #print e  #possibly our code is not going here??? why not printing out word is??
    header = BeautifulSoup(html.text).title.string

    tokens = PunktWordTokenizer().tokenize(header)
    #stop = stopwords.words('english')

    
    for t in tokens:
        t = t.lower()
	if t.isalpha():
	  #and t not in stop:
	  print "word is: " + t
          return t
    return ''

if __name__ == '__main__':
    di_list = get_dinosaurs()
    save_list(di_list, sys.argv[1]) 
