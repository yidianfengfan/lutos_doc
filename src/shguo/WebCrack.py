#-*- coding:utf-8 -*-

import urllib2

directory_file = "home/leishouguo/snoopwap/dir/900.txt" 
#proxy_handler = urllib2.ProxyHandler({'http': 'http://192.168.1.1/'})

proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'admin', 'password')
 
opener = urllib2.build_opener(proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
f = opener.open('http://192.168.1.1')

print dir(f)


