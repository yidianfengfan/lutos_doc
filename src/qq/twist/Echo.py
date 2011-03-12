'''
Created on 2011-3-2

@author: leishg
'''

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.selectreactor import SelectReactor
import sys

class Echo(Protocol):
    '''
    classdocs
    '''
    def connectionMade(self):
        print "connect...."
        #self.transport.loseConnection()

    def connectionLost(self, reason):
        print "close..."

    def dataReceived(self, data):
        self.transport.write(data)
        
def makeQOTDFactory(quote=None):
    factory = Factory()
    factory.protocol = Echo
    factory.quote = quote or 'An apple a day keeps the doctor away'
    return factory

#reactor = SelectReactor()
print sys.modules
reactor.listenTCP(8007, makeQOTDFactory("configurable quote"))
reactor.run()




        
        