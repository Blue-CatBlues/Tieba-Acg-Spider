SPIDER_MODULES = ['spider2024.spiders']
NEWSPIDER_MODULE = 'spider2024.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'spider2024.pipelines.ExcelPipeline': 300,
}