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


class HttpTail:
	
	def __init__(self):
		self.start = 0
		self.step = 1000
		self.end = 1
		self.contentLength = 1000
		self.isGetHead = False
		
	def body(self, buf):
		sys.stdout.write(buf)
	
	def header(self, buf):
		p = re.compile('Content-Range: bytes (\d+)-(\d+)/(\d+)')
		m = p.match(buf)
		if m:
			self.contentLength = int(m.group(3))
			#print start, "  ", step
			if self.start == 0: #first time go to end
				self.start = self.contentLength - 100
				self.end =  self.contentLength
			else:	
				if not self.isGetHead:
					self.start =  self.end + 1
				self.end = self.end + self.step
				if(self.end > self.contentLength):
					self.end = self.contentLength
			
	def getHead(self):
		return 	self.start > self.end
		
				
		
if __name__  == '__main__':
	httpTail =  HttpTail()
	


	while True:
		#print start, "  ", end , "   ", contentLength
		if httpTail.getHead():
			httpTail.isGetHead = True
			print httpTail.start, "  ", httpTail.end , "   ", httpTail.contentLength
			c.setopt(pycurl.NOBODY, 1)
			c.setopt(pycurl.RANGE, '%d-%d' % (1, 2))
		else:
			httpTail.isGetHead = False
			c.setopt(pycurl.NOBODY, 0)
			c.setopt(pycurl.WRITEFUNCTION, httpTail.body)
			c.setopt(pycurl.RANGE, '%d-%d' % (httpTail.start, httpTail.end))
			
		c.setopt(pycurl.HEADERFUNCTION, httpTail.header)
		c.perform()
		
		time.sleep(1)
	

