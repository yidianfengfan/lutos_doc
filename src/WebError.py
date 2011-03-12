'''
Created on 2011-3-12

@author: leishouguo
'''
from bottle import error


@error(404)
def error404(error):
    return 'Nothing here, sorry'
