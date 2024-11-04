# -*- coding: utf-8 -*-

# Scrapy settings for travelspider project

BOT_NAME = 'travelspider'

SPIDER_MODULES = ['travelspider.spiders']
NEWSPIDER_MODULE = 'travelspider.spiders'


ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
   'travelspider.pipelines.ExcelPipeline': 300,
}



