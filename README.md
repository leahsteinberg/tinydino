### (probably) The World's First Dinosaur-Themed Link Shortener.

We're sick of link shorteners that spit out random strings. Tiny dino turns your link www.hackerschool.com/lots-of-random-stuff-here-that-makes-it-really-really-long into something like.... *www.tinydino.com/hackersaurus*

We scraped the dinosaur wikipedia page and did some language processing to find valid dinosaur suffixes and their respective frequency. Each new link is assigned a dinosaur suffix (according to how common that suffix is in the dinosaur corpus). We scrape the website itself for its first 'key word' and attach that to the suffix. We make sure every link is unique.

#### To Do:
* fix Postgres on Heroku to get this online.
