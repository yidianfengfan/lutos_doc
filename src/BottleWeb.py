'''
Created on 2011-3-12

@author: leishouguo
'''

from bottle import run, route, request, response, static_file, abort, redirect, \
    template, view
import WebError


#http://localhost:8080/hello/shguo
@route('/hello/:name')
def hello(name='World'):
    response.content_type = 'text/html; charset=gbk'
    response.headers['Content-Language'] = 'en'
    
    page = request.GET.get('page', '1')
    ip = request.environ.get('REMOTE_ADDR')
    #ip = request.get('REMOTE_ADDR')
    #ip = request['REMOTE_ADDR']
    
    print ip, page, request.header['User-Agent']

    if request.get('X-Requested-With') == 'XMLHttpRequest':
        return 'This is an AJAX request'
    
    
    print "cookie: %s" %(request.get_cookie("visited"))
    if request.get_cookie("visited", 'shguo') == 'yes':
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", u"yes", 'shguo', path="/", expires=3600)

    return '<b>Hello %s!</b>'  % (name)

@route('/')
@route('/index.html')
@route('/index')
def index():
    return "<a href='/hello/shguo'>Go to Hello World page</a>"


#http://localhost:8080/object/100023
@route('/object/:id#[0-9]+#')
def view_object(id):
    return "Object ID: %d" % int(id)


@route('/login', method='POST')
def login_submit():
    name     = request.forms('name')
    password = request.forms('password')
    if check_login(name, password):
        return "<p>Your login was correct</p>"
    else:
        return "<p>Login failed</p>"

def check_login(name, password):
    return name == 'shguo'

@route('/download/:filename')
def download(filename):
    return static_file(filename, root='/path/to/static/files', download=filename)

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")
    
@route('/error')
def wrong():
    redirect("/index")
    

@route('/tpl')
@route('/tpl/:name')
def tpl(name='World'):
    return template('hello_template', name=name)

@route('/tpl1')
@route('/tpl1/:name')
@view('hello_template')
def tpl1(name='World'):
    return dict(name=name)






if __name__ == '__main__':
    import bottle
    app = bottle.default_app()
   
    print template('hello_template', name='shguo')
    print template('Hello {{name.title() if name else "stranger"}}!', name=None)
    print template('Hello {{name.upper() if name else "stranger"}}!', name='mA<r>C')
    print template('Hello {{!name.upper() if name else "stranger"}}!', name='mA<r>C')
    
    run(host='localhost', port=8080)
    


