#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl,sys
import time
import re

httpAddress = "http://www.python.org/"
if len(sys.argv) > 1:
	httpAddress = sys.argv[1]
c = pycurl.Curl()
c.setopt(pycurl.URL, httpAddress)
c.setopt(pycurl.HTTPHEADER, ["Accept:"])

#连接超时设置
c.setopt(pycurl.CONNECTTIMEOUT, 60)
c.setopt(pycurl.TIMEOUT, 300)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)

#模拟浏览器
c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")

#c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
#c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)

import StringIO
b = StringIO.StringIO()

start = 0
step = 1000
end = start + step
contentLength = 1999
shouldGetHead = False

## Callback function invoked when body data is ready
def body(buf):
	# Print body data to stdout
	import sys
	sys.stdout.write(buf)
	# Returning None implies that all bytes were written

## Callback function invoked when header data is ready
def header(buf):
	# Print header data to stderr
	# Content-Range: bytes 2500-2999/18520
	import sys
	#sys.stderr.write(buf)
	
	p = re.compile('Content-Range: bytes (\d+)-(\d+)/(\d+)')
	m = p.match(buf)
	if m:
		global start,end, contentLength, shouldGetHead, step
		contentLength = int(m.group(3))
		#print start, "  ", step
		if(contentLength > end):
			start =  end + 1
			end = end + step
			if(end > contentLength):
				end = contentLength
				shouldGetHead = True
		
		
	# Returning None implies that all bytes were written

 ## Callback function invoked when download/upload has progress
def progress(download_t, download_d, upload_t, upload_d):
	print "Total to download", download_t
	print "Total downloaded", download_d
	print "Total to upload", upload_t
	print "Total uploaded", upload_d


while True:
	#print start, "  ", end , "   ", contentLength
	if shouldGetHead and end >= contentLength:
		c.setopt(pycurl.NOBODY, 1)
		c.setopt(pycurl.RANGE, '%d-%d' % (1, 2))
	else:
		c.setopt(pycurl.WRITEFUNCTION, body)
		c.setopt(pycurl.RANGE, '%d-%d' % (start, end))
		
	c.setopt(pycurl.HEADERFUNCTION, header)
	#c.setopt(c.NOPROGRESS, 0)
	#c.setopt(c.PROGRESSFUNCTION, progress)
	
	#访问,阻塞到访问结束	
	c.perform()
	#print b.getvalue()
	
	#打印出 200(HTTP状态码)
	#print c.getinfo(pycurl.HTTP_CODE)
	
	time.sleep(1)
	

