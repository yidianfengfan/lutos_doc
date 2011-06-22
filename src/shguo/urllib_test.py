#-*- coding:utf-8 -*-

import urllib2
 
proxy_handler = urllib2.ProxyHandler({'http': 'http://www.pythonclub.org:3128/'})
proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
 
opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
f = opener.open('http://www.example.com/login.html')
content = f.read()
print content