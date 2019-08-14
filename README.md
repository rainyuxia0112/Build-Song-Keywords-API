# Build-Song-Keywords-API

* Writing SQL queries to compute the TF-IDF score for each token in each song;
* Using psycopg2 package to connect database from local host;
* Using cursor to get song-names for certain keywords (song title is sorted according to the score);
* Using flask to build API for keywords searching;

# Get Started

- Preparation

* This duty needs to be done in python3.X environment

* Needs to activate a new python environment

```shell
source ./bin/activate   
```

- Installtion

```shell
pip3 install -r requirement.txt 
```
* Note：[flask](http://flask.pocoo.org/)

```shell
FLASK_APP=app2.py flask run 
* Serving Flask app "app2"
* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

# Introduction to this api

|URL|Method|Return
|----|--------|----
|*http://144.202.28.242:8000/*|GET|
|*http://144.202.28.242/api/resources/search?type={}:8000*|GET|get song names that are included keywords
|*http://144.202.28.242/api/resources/search?name={}:8000*|GET|get a perticular song's keywords

Authors
* Yu Xia

in collaboration with 
[peterljw](https://github.com/peterljw)
