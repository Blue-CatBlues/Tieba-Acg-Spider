SPIDER_MODULES = ['spider2107.spiders']
NEWSPIDER_MODULE = 'spider2107.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'spider2107.pipelines.ExcelPipeline': 300,
}
