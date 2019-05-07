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

## Rsult :

[
  {
    "Miracle": 15.0514997831991
  }, 
  {
    "Our Love Was": 15.0514997831991
  }, 
  {
    "The Passion": 15.0514997831991
  }, 
  {
    "Oye Baby": 15.0514997831991
  }, 
  {
    "To Love Somebody": 15.0514997831991
  }, 
  {
    "I Wanna Little Love": 15.0514997831991
  }, 
  {
    "Heartbreaker": 15.0514997831991
  }, 
  {
    "I Love You Too Much": 14.7504697875351
  }, 
  {
    "Calling Dr. Love": 14.7504697875351
  }, 
  {
    "Let Me Take You In My Arms Again": 14.7504697875351
  }, 
  {
    "Fool For Your Love": 14.7504697875351
  }, 
  {
    "How To Love": 14.7504697875351
  }, 
  {
    "Path Of The Right Love": 14.7504697875351
  }, 
  {
    "Let The Idiot Speak": 14.7504697875351
  }, 
  {
    "Love Don't Live Here Anymore": 14.7504697875351
  }, 
  {
    "Somebody Like You": 14.7504697875351
  }, 
  {
    "Tell Me That You Love It": 14.7504697875351
  }, 
  {
    "Believe In Love": 14.7504697875351
  }, 
  {
    "Nobody": 14.7504697875351
  }, 
  {
    "Let Everything That Has Breath": 14.4494397918711
  }
]

## Built With
* [flask](http://flask.pocoo.org/)
* [psycopg2](http://initd.org/psycopg/) - python package for postgres

## Authors
* Yu Xia
