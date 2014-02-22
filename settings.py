# Scrapy settings for byellow project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'byellow'

SPIDER_MODULES = ['byellow.spiders']
NEWSPIDER_MODULE = 'byellow.spiders'
ITEM_PIPELINES = {'byellow.pipelines.ByellowPipeline': 300,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'byellow (+http://www.yourdomain.com)'
