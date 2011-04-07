#encoding: utf-8
'''
Created on 2011-3-17
k
@author: leishouguo
'''
from history.HistoryModel import HistoryModel, obj2dict

class MongoManger(object):
    db = None
    def __init__(self, host, port, dbName):
        self.host = host
        self.port = port
        self.dbName = dbName
    
    
    def getFs(self, tableName):
        """
            get gridFS
        """
        import gridfs
        if self.db is None:
            self.db = self.getDb(self.dbName)
        return gridfs.GridFS(self.db, tableName)

    def getDb(self,  dbName):
        """
            get monogdb
        """
        from pymongo import Connection
        c = Connection(self.host, self.port)
        return c[dbName]
    

    def getCollection(self, tableName):
        if self.db is None:
            self.db = self.getDb(self.dbName)
        return self.db[tableName]
    
    def getTableByName(self, tableName):
        if self.db is None:
            self.db = self.getDb(self.dbName)
        return self.db[tableName]
    
    
    def close(self):
        if(self.db is not None):
            self.db.close()
            
            
        
    def store(self, tableName,values):
        table = self.getCollection(tableName)
        print table
        print(table.insert(values))
        
     
    def find(self, tableName):
        table = self.getCollection(tableName)   
        print table
        records = table.find()
        for v in records:
            print v
    
if __name__ == '__main__':
    print "start server...."
    #Connection("mongodb://morton.local:27017,morton.local:27018,morton.local:27019")
    host = "mongodb://shguo:shguo@localhost:27017/shguo"
    dbName = "shguo"
    tableName = "his"
    
    mongoUtils = MongoManger(host, 27017, dbName)
    
    m = HistoryModel("清", "顺治", 1638, 1, 1651, 2)
    mongoUtils.store(tableName, obj2dict(m))
    
    mongoUtils.find(tableName)
    
    
    
