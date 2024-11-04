import scrapy

class TiebaItem(scrapy.Item):
    name = scrapy.Field()
    member = scrapy.Field()
    comment = scrapy.Field()
    main = scrapy.Field()