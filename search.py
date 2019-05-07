#!/usr/bin/env python
import psycopg2
import re
import string
import sys
_PUNCTUATION = frozenset(string.punctuation)

def _remove_punc(token):
    """Removes punctuation from start/end of token."""
    i = 0
    j = len(token) - 1
    idone = False
    jdone = False
    while i <= j and not (idone and jdone):
        if token[i] in _PUNCTUATION and not idone:
            i += 1
        else:
            idone = True
        if token[j] in _PUNCTUATION and not jdone:
            j -= 1
        else:
            jdone = True
    return "" if i > j else token[i:(j+1)]

def _get_tokens(query):
    rewritten_query = []
    tokens = re.split('[ \n\r]+', query)
    for token in tokens:
        cleaned_token = _remove_punc(token)
        if cleaned_token:
            if "'" in cleaned_token:
                cleaned_token = cleaned_token.replace("'", "''")
            rewritten_query.append(cleaned_token)
    return rewritten_query



def search(query, query_type):
    
    rewritten_query = _get_tokens(query)
    rows = []
    try:
        connection = psycopg2.connect(host='localhost', user='rain',port='8888',
                                  database='postgres', password='xiayu960112')
        cursor=connection.cursor()
        if query_type=='or':
            sql='select s.song_name, SUM(score) FROM tfidf t JOIN song s ON s.song_id=t.song_id WHERE token= ANY (%s) GROUP BY s.song_name ORDER BY SUM(score) DESC;'
            cursor.execute(sql, (rewritten_query,))
            rows = cursor.fetchall()
        if query_type == 'and':
            str='WHERE (t.song_id in ('
            for ele in rewritten_query:
                tr=' '+'select song_id from tfidf where'+' '+'token=' +"'"+ ele+"'"
                str=str+ tr + ' '+'INTERSECT'
            str=str[:-9] + ')'  
            str=str+' '+'AND token= ANY (%s))'
            sql='select s.song_name, SUM(score) FROM tfidf t JOIN song s ON s.song_id=t.song_id'+' '+str+' '+'GROUP BY s.song_name ORDER BY SUM(score) DESC;'
            cursor.execute(sql, (rewritten_query,))
            rows = cursor.fetchall()    
                                    
    except (Exception,psycopg2.DatabaseError) as error:
        print (error)

    finally:
        if connection is not None:
            connection.close()                                
    return rows  
