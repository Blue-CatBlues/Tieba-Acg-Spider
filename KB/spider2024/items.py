import scrapy

class actor_link(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

