#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2011-3-12

@author: Administrator
'''

from TriTree import TrieTree
from bottle import route, template, run, send_file, request
import bottle

trieTree = TrieTree()
trieTree.add("a")
trieTree.add("ab")
trieTree.add("ac")

@route("/")
@route("/index.html")
def index():
    return template('index.html')
    #return send_file('views/index.html', root = './')
    

@route("/add")
def add():
    word = request.GET.get("word");
    word = word.decode("utf8")
    print word
    if word and len(word) > 0:
        trieTree.add(word)
        return {'success': True}    
    return {'success': False}

@route("/check")
def check():
    word = request.GET.get("word");
    word = word.decode("utf8")
    print word
    if word and len(word) > 0:
        if trieTree.has_word(word):
            return {'success': True}
    return {'success': False}

@route("/remove")
def remove():
    word = request.GET.get("word");
    word = word.decode("utf8")
    if word and len(word) > 0:
        trieTree.remove(word)
        return {'success': True}    
    return {'success': False}

@route("/black", method=['GET','POST'])
def black():
    word = request.GET.get("word");
    word = request.POST.get("word", None) #request.forms.get("word", None);
    print word

    word = word.decode("utf8")
    print "====>", word
    if word and len(word) > 0:
        result = trieTree.black(word)
        print trieTree.data
        return {'success': True, 'msg': result}    
    return {'success': False, 'msg': 'error'}


class StripPathMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.app(e,h)



 
if __name__ == '__main__':
    word = '中国人'
    print word
    print word.decode("utf8")
    
    uword = u'中国人'
    print uword
    print uword.decode("utf8")
    try:
        uword.text()
    except Exception,data:
        print data
    
    #app = bottle.app()
    #myapp = StripPathMiddleware(app)
    print trieTree.data
    bottle.app().catchall = False #if exception not 500
    bottle.debug(True)
    bottle.run(host='localhost', port=8080, reloader=False)
 