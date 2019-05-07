#!flask/bin/python
# -*- coding: utf-8 -*-
import sys
import flask
from flask import request, jsonify
import search

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for song names using TFIDF.</p>'''


@app.route('/api/v1/resources/songs', methods=['GET'])
def api_query():
    # Check if an query was provided as part of the URL.
    # If query is provided, assign it to a variable.
    # If no query is provided, display an error in the browser.
    if 'query' in request.args:
        query= (request.args['query'])
    else:
        return "Error: No keyword provided. Please specify keywords."
    if 'type' in request.args:
        query_type= (request.args['type'])
    else:
        return "Error: No query_type field provided. Please specify an query_type."

    if 'page' in request.args:
        page= int(request.args['page'])
    else:
        page=1

    if 'button' in request.args:
        button= (request.args['button'])
    else:
        button=''

    # 根据上述信息搜索信息，形成api传输出来
    if button=='next':
        page=page+1
    if button=='previous':
        page=page-1
    else:
        page=page
    results = []
    total= search.search(query, query_type)
    if (page)*20<=len(total):
        rows=total[(page-1)*20:page*20]
    else:
        rows=total[(page-1)*20:]           
    for row in rows:
        results.append(dict([row]))
    

    # Loop through the data and match results that fit the requested query and query type.
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
