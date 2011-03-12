'''
Created on 2011-3-9

@author: Administrator
'''

from cgi import parse_qs, escape
import re

def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('301 MOVE', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
    Hello %(subject)s!
''' % {'subject': subject}]


def index(environ, start_response):
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello World Application
               This is the Hello World application:

`continue <hello/>`_

''']

def hello(environ, start_response):
    """Like the example above, but it uses the name specified in the
URL."""
    # get the name from the url if it was specified there.
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!

''' % {'subject': subject}]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

# map urls to functions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)



if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    
    #srv = make_server('localhost', 8080, hello_world)
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
