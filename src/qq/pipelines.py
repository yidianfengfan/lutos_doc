# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.core.engine import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3
from os import path
from scrapy import log
from qq.items import QqContentItem


class QqPipeline(object):
    filename = 'data.sqlite'
    path = None
    def __init__(self):
        log.msg("test log for init", log.INFO)
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
 
    def process_item(self, item, spider):
        #print "===================================", item
        if type(item) is QqContentItem:
            print "is content===>%s" %(item['url'])
        else:    
            self.conn.execute('insert into blog values(?,?,?)', 
                          (item['bookName'].__str__(), item['bookAuthor'].__str__(), 'sdfsdffsdf'))
        return item
 
    def initialize(self):
        
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
 
    def create_table(self, filename):
        log.msg("====create table ", log.ERROR)
        conn = sqlite3.connect(filename)
        conn.execute("""create table blog
                     (url text , raw text, domain text)""")
        conn.commit()
        return conn
    
    def spider_opened(self, spider):
        print '====spider opened===='
        
    def spider_closed(self, spider):
        print '====spider closed===='
    
    
