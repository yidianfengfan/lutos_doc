# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class QqItem(Item):
    # define the fields for your item here like:
    id = Field()
    url = Field()
    bookName = Field()
    bookAuthor = Field()
    part = Field()
    
    #pass

class QqContentItem(QqItem):
    title = Field()
    content = Field()
    url = Field()
    def __init__(self):
        QqItem.__init__(self)
        
    def __str__(self):
        return self['url']
 
class QqPartItem(Item):
    partTitle = Field()
    contents = Field()   
    def __str__(self):
        return self['partTitle']