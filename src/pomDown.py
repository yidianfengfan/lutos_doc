#!/usr/bin/python
#encoding: utf-8
import sys
import urllib2


repoUrl = "http://repo1.maven.org/maven2/"
repoDir = "/home/leishouguo/.m2/repository"




def downMvnJar(groupId, artifactId, version):
	groupIdStr = groupId.replace(".", "/")
	
	url = repoUrl + groupIdStr + "/" + artifactId + "/" + version + "/";
	repo = repoDir + "/" + groupIdStr + "/" + artifactId  + "/" + version;
	
	from os import makedirs, path
	from shutil import rmtree
	
	if path.exists(repo):
		rmtree(repo)
	
	if not path.exists(repo):
		makedirs(repo)
			
	
	
	jarName = artifactId+"-"+version + ".jar";
	print "get jar from {0}".format(url + jarName)
	
	req = urllib2.Request(url + jarName)
	response = urllib2.urlopen(req)
	result = response.read()
	jarFile = file(repo + "/" + jarName, "w")
	jarFile.write(result)
	jarFile.close()

	pomName = artifactId+"-"+version + ".pom";
	print "get pom from {0}".format(url + pomName)
	
	req = urllib2.Request(url + pomName)
	response = urllib2.urlopen(req)
	result = response.read()
	f = file(repo + "/" + pomName, "w")
	f.write(result)
	f.close()
	
	
	sourcesName = artifactId+"-"+version + "-sources.jar";
	print "get sources from {0}".format(url + sourcesName)
	
	req = urllib2.Request(url + sourcesName)
	response = urllib2.urlopen(req)
	result = response.read()
	f = file(repo + "/" + sourcesName, "w")
	f.write(result)
	f.close()

def header(buf):
	# Print header data to stderr
	import sys
	sys.stderr.write(buf)
	# Returning None implies that all bytes were written

'''
WRITEFUNCTION(string) -> number of characters written
READFUNCTION(number of characters to read)-> string
HEADERFUNCTION(string) -> number of characters written
PROGRESSFUNCTION(download total, downloaded, upload total, uploaded) -> status
DEBUGFUNCTION(debug message type, debug message string) -> None
'''
	
if __name__ == '__main__':
	import pycurl
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://www.python.org/")
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	import StringIO
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.HEADERFUNCTION, header)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	print b.getvalue()

	
	
	print sys.argv	
	
	if(len(sys.argv) != 4 ):
		print "参数错误"
		sys.exit(10)
	
	
	downMvnJar(sys.argv[1], sys.argv[2], sys.argv[3])
