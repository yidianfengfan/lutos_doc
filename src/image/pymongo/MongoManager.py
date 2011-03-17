#encoding: utf-8
'''
Created on 2011-3-17
k加
@author: leishouguo
'''
from image.pymongo import ImageUtil
import re
import Config
config = Config.Config()

class MongoManger(object):
    db = None
    def __init__(self):
        pass
    
    
    def getFs(self, server, port,  dbName, tableName):
        """
            get gridFS
        """
        import gridfs
        if self.db is None:
            self.db = self.getDb(server, port,  dbName)
        return gridfs.GridFS(self.db, tableName)

    def getDb(self, server, port,  dbName):
        """
            get monogdb
        """
        from pymongo import Connection
        c = Connection(server, port)
        return c[dbName]
    

    def getCollection(self, server, port,  dbName, tableName):
        if self.db is None:
            self.db = self.getDb(server, port,  dbName)
        cn = '{0}.files'.format(tableName)
        return self.db[cn]
    
    def close(self):
        if(self.db is not None):
            self.db.collection.close()
            
            
        
    def store(self, file, name):
        if not hasattr(file, 'read'):
            raise TypeError("file object error")
       
        data = file.read()
        return self.storeByte(data, name)
    
    def storeByte(self, data, name):
        if (len(data) > int(config.get('max.file.size'))):
            return [False, 'file: {0} too big'.format(name)]
        
        ext = ImageUtil.getImageType(data[:32])
        if ext is None:
            return [False, "invalid image file"]
        print len(data)
        id = ImageUtil.makeId(data)
        print ('id: {0}'.format(id))
        fs = self.getFs(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
        if fs.exists(id):
            print ('id {0}  exists!!'.format(id))
            return [False, 'exists']
        filename = '{0}.{1}'.format(id, ext)
        print ('new filename: %r' % filename)
        return [True, fs.put(data, _id=id, filename=filename,type='jpg', note=name), filename]    
        
    def get(self, id):
        fs = self.getFs(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
        if fs.exists(id):
            return fs.get(id)
    
    def delete(self, id):
        fs = self.getFs(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
        fs.delete(id)
        if fs.exists(id):
            return False
        return True    
    
    def exists(self, hashed):
        """check special hash value """
        coll = self.getCollection(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
        return coll.findOne([('md5', hashed)])
    
    def browse(self, limit=20, start=0):
        """retrieve files from mongodb for gallery"""
        #return getFs().list()
        sort = [('updateDate',-1)]
        coll = self.getCollection(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
        cursor = coll.find(limit=limit, skip=start, sort=sort)
        items = []
        for item in cursor:
            items.append(self.makeItem(item))
        return {'items':items,'total':cursor.count()}
    
    def makeItem(self, item):
        newItem = item.copy()
        newItem['id'] = newItem.pop('_id')
        newItem['created'] = newItem.pop('uploadDate')
        newItem.pop('chunkSize', None)
        newItem.pop('app_id', None)
        return newItem
    
if __name__ == '__main__':
    mongoManager = MongoManger()
    fs = mongoManager.getFs(config.get("mongo.server"), int(config.get("mongo.port")), config.get("mongo.database"), config.get("mongo.collection"))
    print fs
    
    data = mongoManager.store(file("/usr/local/src/linux-soft/image/s290x360_mLbmkJbmiLcozLcG.jpg"), "s290x360_mLbmkJbmiLcozLcG.jpg")
    print data
    
    print mongoManager.get("ed298kgybcccr6e5rmck67o61")
    
    print mongoManager.browse(10, 0)
    
    
    