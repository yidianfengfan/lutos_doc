#!/usr/bin/python
# encoding: utf-8
from HTMLParser import HTMLParser
from cookielib import CookieJar
import cookielib
import urllib
import urllib2



cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

loginUrl = "https://passport.360buy.com/new/LoginService.aspx"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }


values = {
	'uid':'uid',
	'loginpwd':'leiguo12',
	'loginname': 'leishguo'
		}

data = urllib.urlencode(values)


def getuid():
	print "get uid from{0}".format("jingdong")
	url = "https://passport.360buy.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fwww.360buy.com%2F"
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	result = response.read()
	print result

def login():
	req = urllib2.Request(loginUrl, data, headers)
	response = opener.open(req)
	result = response.read()
	print result



class HTTPRefererProcessor(urllib2.BaseHandler):
    def __init__(self):
        self.referer = None 


    def http_request(self, request):
        if ((self.referer is not None) and
            not request.has_header("Referer")):
            request.add_unredirected_header("Referer", self.referer)
        return request 


    def http_response(self, request, response):
        self.referer = response.geturl()
        return response 


    https_request = http_request
    https_response = http_response 

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        print "Encountered the end of a %s tag" % tag


def main():
    cj = CookieJar()
    opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(cj),
        HTTPRefererProcessor(),
    )
    urllib2.install_opener(opener) 
    
if __name__ == '__main__':
    #getuid()
    for c in cj:
    	print c
    #login()
    
    for c in cj:
    	print c
    	
    print '----finished----'

