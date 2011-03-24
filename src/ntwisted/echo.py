#切换行号显示

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class HelloHD(Protocol):

    def connectionMade(self):
        self.transport.write("Hello This is HD's Test protocol\r\n") 
        self.transport.loseConnection()


# 下面就是施展Twisted神奇的代码了
factory = Factory()
factory.protocol = HelloHD

# 侦听运行于8025端口，最好是一个大于1024的端口
reactor.listenTCP(8025, factory)
reactor.run()
