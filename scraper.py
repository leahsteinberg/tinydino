import requests
from BeautifulSoup import BeautifulSoup
import sys

def get_dinosaurs():
    di_list = []
    html = requests.get('http://en.wikipedia.org/wiki/List_of_dinosaurs').content
    
    soup = BeautifulSoup(html)
    possible_names = soup.findAll('i')
    for name in possible_names:
        a = name.find('a')
        if a is not None:
            di_list.append(name.text)

    return di_list

def save_list(list, filepath):
    f = open(filepath, 'w')
    for l in list:
        if l.strip() != '':
            f.write(l + '\n')  
    f.close()

if __name__ == '__main__':
    di_list = get_dinosaurs()
    save_list(di_list, sys.argv[1]) 