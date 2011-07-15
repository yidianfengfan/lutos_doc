#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl,sys
import time
import re
#http://soa.user.360buy.com/logs/sns.u.soa-ice.log
#http://172.16.112.234/soalogs/sns.u.soa.log
#sudo tcpdump -i eth4 port 80 


httpAddress = "http://soa.user.360buy.com/logs/sns.u.soa-ice.log"
if len(sys.argv) > 1:
	httpAddress = sys.argv[1]
c = pycurl.Curl()
c.setopt(pycurl.URL, httpAddress)
c.setopt(pycurl.HTTPHEADER, ["Accept:"])

c.setopt(pycurl.CONNECTTIMEOUT, 60)
c.setopt(pycurl.TIMEOUT, 300)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)

c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")

#c.setopt(pycurl.PROXY, ￢ﾀﾘhttp://11.11.11.11:8080￢ﾀﾲ)
#c.setopt(pycurl.PROXYUSERPWD, ￢ﾀﾘaaa:aaa￢ﾀﾙ)

start = 0
step = 1000
end = 1
contentLength = 1000
isGetHead = False

def body(buf):
	sys.stdout.write(buf)

def header(buf):
	p = re.compile('Content-Range: bytes (\d+)-(\d+)/(\d+)')
	m = p.match(buf)
	if m:
		global start,end, contentLength, isGetHead, step
		contentLength = int(m.group(3))
		#print start, "  ", step
		if start == 0: #first time go to end
			start = contentLength - 100
			end =  contentLength
		else:	
			if not isGetHead:
				start =  end + 1
			end = end + step
			if(end > contentLength):
				end = contentLength
			
					
		

while True:
	#print start, "  ", end , "   ", contentLength
	if start > end:
		isGetHead = True
		print start, "  ", end , "   ", contentLength
		c.setopt(pycurl.NOBODY, 1)
		c.setopt(pycurl.RANGE, '%d-%d' % (1, 2))
	else:
		isGetHead = False
		c.setopt(pycurl.NOBODY, 0)
		c.setopt(pycurl.WRITEFUNCTION, body)
		c.setopt(pycurl.RANGE, '%d-%d' % (start, end))
		
	c.setopt(pycurl.HEADERFUNCTION, header)
	c.perform()
	time.sleep(1)
	

