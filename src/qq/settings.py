# Scrapy settings for qq project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'qq'
BOT_VERSION = '1.0'

DOWNLOAD_DELAY = 2
CONCURRENT_ITEMS = 500 #Maximum number of concurrent items (per response) to process
LOG_LEVEL = 'INFO'
SCHEDULER = 'scrapy.core.scheduler.Scheduler'

#DUPEFILTER_CLASS = 'scrapy.core.scheduler.Scheduler'
SCHEDULER_MIDDLEWARES_BASE = {
    'scrapy.contrib.schedulermiddleware.duplicatesfilter.DuplicatesFilterMiddleware': 500,
}



SPIDER_MODULES = ['qq.spiders']
NEWSPIDER_MODULE = 'qq.spiders'
DEFAULT_ITEM_CLASS = 'qq.items.QqItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['qq.pipelines.QqPipeline']



