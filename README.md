# The World's First Dinosaur-Themed Link Shortener.

### What it does
We're sick of link shorteners that spit out random strings. Tiny dino turns your link hackerschool.com/lots-of-random-stuff-here-that-makes-it-really-really-long into something like.... *tinydino.com/hackersaurus*

### How it works
To build this, we scraped the dinosaur wikipedia page and did some language processing (stemming) to find valid dinosaur suffixes and their respective frequencies. Each new link is assigned a dinosaur suffix (according to how common that suffix is in the dinosaur corpus). Then it scrapes the website of the long url for its first 'key word' and attach that to the suffix. Every dino-link is unique. The short and long urls are saved in a database.

### How to use it
Go to www.lil-dino.com to shorten any link.


### To Do:
* draw picture of a dinosaur to make the website even better.
