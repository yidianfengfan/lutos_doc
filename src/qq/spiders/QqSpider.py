'''
Created on 2011-2-25

@author: leishg
scrapy startproject qq
scrapy crawl book.qq.com
scrapy crawl book.qq.com --set FEED_URI=items.json --set FEED_FORMAT=json

create a new spider:
scrapy genspider -l
scrapy genspider -d basic
scrapy genspider -t basic QqSpider book.qq.com

scrapy server
scrapy list   -- list spider

scrapy fetch --nolog --headers http://www.example.com/
scrapy view  http://www.360buy.com/  ##download and view in browser
scrapy shell  http://www.360buy.com/  ##download and view in browser
scrapy parse  http://www.360buy.com/ --callback --rules --noitems --nolinks

HtmlXPathSelector XmlXPathSelector
'''

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from qq.items import QqItem, QqContentItem, QqPartItem
import time
from scrapy.http.response import Response

class QqSpider(BaseSpider):
    
    name = "book.qq.com"
    allowed_domains = [name]
    start_urls = [
       "http://bookapp.book.qq.com/origin/workintro/364/work_2318700.shtml"
    ]
    
    @staticmethod
    def write(response):
        filename = response.url.split("/")[-1]
        filename = "F:/temp/" + filename
        print "fileName====>%s" %filename
        open(filename, 'wb').write(response.body)
        
    def parse(self, response):
        
        QqSpider.write(response)
                
        hxs = HtmlXPathSelector(response)
        
        items = []
        
        item = QqItem()
        
        item['id'] = time.time()
        item['url'] = response.url
        
        bookNameXpath = "//div[3]/div/div/div/h1/a/text()"
        bookName = hxs.select(bookNameXpath).extract()
        item['bookName'] = bookName
        #print "crawler book.qq.com ====>>>>>>>" , bookName
        
        bookAuthorXpath = "//div[3]/div/div/div/span/a/text()"
        bookAuthor = hxs.select(bookAuthorXpath).extract()
        item['bookAuthor'] = bookAuthor
        #print "crawler book.qq.com ====>>>>>>>" , bookAuthor
        
        partXpath = '//div[@id="book_detail"]'
        partSel = hxs.select(partXpath)
        
        titleXpath = "h3/text()"
        title = partSel.select(titleXpath).extract()
        print "title length===>", len(title)
        part = []
        for e in title:
            print "title===>", e
            partItem = QqPartItem()
            partItem['partTitle'] = e
            partItem['contents'] = []
            part.append(partItem)
            
        
        item['part'] = part
            
        contentXpath = "ol[@class='clearfix']"
        content = partSel.select(contentXpath)
        #print "content length===>", len(content)
       
        for num in range(len(content)):
            e = content[num]
            partItem = part[num]
            
            #print "content===>", e
            contentLinkXpath = "li/a/@href"
            contentLink = e.select(contentLinkXpath).extract()
            
            contentTitleXpath = "li/a/text()"
            contentTitle = e.select(contentTitleXpath).extract()
            baseNum = self.getBaseNum(response.url)
            #print 'baseNum===>%s' %(baseNum)
            contentLink = [self.checkUrl(n, baseNum) for n in contentLink]
            
            #print "===>%s===>%s" %(contentTitle, contentLink)
            
            
            #add to part
            for contentNum in range(len(contentLink)):
                contentItem = QqContentItem()
                contentItem['url'] = contentLink[contentNum]
                contentItem['title'] = contentTitle[contentNum]
                partItem['contents'].append(contentItem)
            
            items.extend([self.make_requests_from_url(url).replace(callback=self.parse_content) for url in contentLink])
            
        #posts = hxs.select('//ul/li/a/@href').extract()
        #items.extend([self.make_requests_from_url(url).replace(callback=self.parse_post) for url in posts])
        
        print "items====>", item
        items.append(item)
        
        return items
    
    
    def parse_content(self, response):
        QqSpider.write(response)
        
        hxs = HtmlXPathSelector(response)
        
        contentXpath = '//div[@id="content"]/text()'
        content = hxs.select(contentXpath).extract()
        contentItem = QqContentItem()
        contentItem['content'] = content
        contentItem['url'] = response.url
        pass
        return contentItem
    
    def getBaseNum(self, url):
        import re
        r = re.compile(r'.*?/(\d+)/')
        return r.search(url).group(1)
    
    def checkUrl(self, url, baseNum):
        import re
        if url[:4] == "http" :
            
            pass
        else:
            url = "http://bookapp.book.qq.com%s" %(url)
        r =   re.compile(r'.*?workid=(\d+).*?chapterid=(\d+)')  
        one = r.search(url).group(1)
        two = r.search(url).group(2)
        
        return "http://bookapp.book.qq.com/origin/workintro/%s/%s/chp_info_%s.htm" %(baseNum, one, two)
        
SPIDER = QqSpider()

