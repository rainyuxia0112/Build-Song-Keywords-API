# Build-Song-Keywords-API


* Writinh SQL queries to compute the TF-IDF score for each token in each song;
* Using psycopg2 package to connect database from local host;
* Using cursor to get song-names for certain keywords (song title is sorted according to the score）
* Using flask to build API for keywords searching

##
How to use it on localhost:
The url is:http://127.0.0.1:5000/api/v1/resources/songs?query={}&type={}&page={}&button={}
query is the keywords to search
type are 'and', 'or'
page is the page to show (limit 20 records one page)
button are 'next', 'previous' to show next page or previous page

## Built With
* [flask](http://flask.pocoo.org/)
* [psycopg2](http://initd.org/psycopg/) - python package for postgres

## Authors
* Yu Xia
