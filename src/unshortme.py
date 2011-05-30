'''
Created on 2011-5-30

http://api.unshort.me/?r=http://tinyurl.com/cn3m36&t=json 

@author: leishouguo
'''
import urllib2;
import simplejson;

api_url_template = 'http://api.unshort.me/?r=%s&t=%s'

def unshortme (url, type):
    api_url = api_url_template %(url, type)
    print 'unshorturl:', api_url
    
    req = urllib2.Request(api_url)
    response = urllib2.urlopen(req)
    result = response.read()
    print result
    
    #Encoding basic Python object hierarchies:
    #simplejson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    #Decoding JSON:
    ss = simplejson.loads(result);
    print ss
    print ss['resolvedURL']
    print ss['success']
    print ss['requestedURL']

if __name__ == '__main__':
    import sys
    #unshortme(sys.argv[1], 'json')
    unshortme('http://tinyurl.com/cn3m36', 'json')