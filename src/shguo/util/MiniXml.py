'''
Created on 2011-5-26

@author: leishouguo
'''

import re
from xml.dom import minidom
 
class MiniXml:
 
    def __init__(self):
        self._dom_ = None
        self._data_ = None
 
    def parseXml(self, encoding):
        d = self.domToDict(self._dom_, encoding, None)
        self._data_=self.loadData(d, '', None)
 
    def loadFile(self, fname):
        f = open(fname, 'r')
        s = f.read()
        f.close()
        self.loadString(s)
        return self
 
    def loadString(self, string):
        if string[:5] == '<?xml':
            ss = string.split('?>', 1)
            m = re.search(r'encoding=\W([\w\-]+)\W', ss[0])
            if m:
                string = ss[1].decode(m.group(1)).encode('utf8')
            else:
                string = ss[1]
        self._dom_ = minidom.parseString(string)
        return self
 
    def domToDict(self, node, encoding='utf8', data=None):
        if data == None:
            data = {}
        if node.nodeType == node.DOCUMENT_NODE:
            self.domToDict(node.firstChild, encoding, data)
            return data
        d = {}
        if node.hasChildNodes():
            for i in node.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    if d.has_key('<text>'):
                        d['<text>'] += i.nodeValue.encode(encoding)
                    else:
                        d['<text>'] = i.nodeValue.encode(encoding)
                elif i.nodeType == i.ELEMENT_NODE:
                    self.domToDict(i, encoding, d)
 
        if node.hasAttributes():
            d['<attrs>'] = dict([(i[0].encode(encoding), i[1].encode(encoding))
                                    for i in node.attributes.items()])
 
        if not node.hasAttributes() and not node.hasChildNodes():
            d['<text>'] = ''
 
        key = node.nodeName.encode(encoding)
        if data.has_key(key):
            if type(data[key]) != list:
                data[key] = [data[key]]
            data[key].append(d)
        else:
            data[key] = d
 
    def loadData(self, d, p, data=None):
        if data == None:
            data = {}
 
        if type(d) == list:
            for dd in d:
                if type(dd) == dict:
                    self.loadData(dd, p, data)
            return None
 
        cs = []
        if d.has_key('<text>'):
            cs.append(d.pop('<text>').strip())
 
        if d.has_key('<attrs>'):
            cs.append(d.pop('<attrs>'))
 
        for c in cs:
            if data.has_key(p):
                if type(data[p]) != list:
                    data[p] = [data[p]]
                data[p].append(c)
            else:
                data[p] = c
 
        for k, v in d.items():
            self.loadData(v, p + '/' + k, data)
 
        return data
 
 
    def get(self, path, df=None):
        return self._data_.get(path, df)
 
    def list(self, path):
        pos = len(path)
        return dict([(i[pos:], self._data_[i]) for i in self._data_ if i.find(path) == 0])
 
    def end(self):
        self._dom_.unlink()
 
 
def parseFile(fname, encoding = 'utf8'):
    _i = MiniXml()
    _i.loadFile(fname).parseXml(encoding)
    _i.end()
    return _i
 
def parseString(string, encoding = 'utf8'):
    _i = MiniXml()
    _i.loadString(string).parseXml(encoding)
    _i.end()
    return _i


if __name__ == '__main__':
    res = '<t><a><b x="1" xx="2" /><b x="1" /></a><k><c x="1" xx="2"/><d hh="xxx"></d><e /></k></t>'
    ixml = parseString(res)
    print ixml.get('/t/a/b') #[{'x': '1', 'xx': '2'}, {'x': '1'}]
    print ixml.list('/t/k/') #{'c': {'x': '1', 'xx': '2'}, 'e': '', 'd': {'hh': 'xxx'}}