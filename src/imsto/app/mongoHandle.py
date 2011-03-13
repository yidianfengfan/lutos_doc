# encoding: utf-8
'''
Created on 2011-3-13

@author: Administrator
'''
from bottle import route, static_file, run, debug

rootdir = "F:/svn/git/jd_book_read/src/imsto/static"

@route('/static/:filename')
def static_file(filename):
    print filename 
    return static_file(filename, root = ['../static/'])

@route("/index.html")
def index():
    return "hello"


if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8080)