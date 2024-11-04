SPIDER_MODULES = ['travelspider.spiders']
NEWSPIDER_MODULE = 'travelspider.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'travelspider.pipelines.ExcelPipeline': 300,
}
