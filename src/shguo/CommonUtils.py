# encoding: utf-8

def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


def info(object, spacing=10, collapse=1): 
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if  callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %  (method.ljust(spacing), processFunc(str(getattr(object,    method).__doc__)))   for method in methodList])

def useful():
    import types
    print type(1) is types.IntType
    print dir(1)
    print str(1)
    print "========================"
    print 1 in [2]
    print [2].count(2)
    try:
        print [2].index(3)
    except  Exception, e:
        print e
    finally:
        print "finally"    
    
    print "========================"
    a = ""
    b = "second"
    print 1 and a or b
    print (1 and [a] or [b])[0]
    print "========================"
    
    #只要有可能,你就应该使用在 os 和 os.path 中的函数进行文件、目录和路径的操作
    import os
    print os.path.expanduser("~")
    print os.path.join("/usr", "hello.txt")
    import glob
    print glob.glob('/usr/*lib*')
    print "========================"
    import re
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    print phonePattern.search('800-555-1212').groups()
    print "========================"
    
    
class UserInfo:
    """ userinfo  from table userinfo and userinfoext
    """
    typeone = 1
    
    def __init__(self, uid, pin):
        self.uid = uid
        self.pin = pin
    
    def toString(self):
        return self.uid , " " , self.pin;    
    
    @staticmethod
    def gen(uid, pin):
        return UserInfo(uid, pin)

if __name__ == "__main__":
    myParams = {
                "server":"mpilgrim",
                "database":"master", 
                "uid":"sa", 
                "pwd":"secret"
    }
    print buildConnectionString(myParams)
    
    print info(myParams)
    
    
    useful()
    
    
    userInfo = UserInfo.gen(1, "shguo");
    print userInfo.toString()
    print UserInfo.typeone
    print getattr(userInfo, "pin")
    
    
    

