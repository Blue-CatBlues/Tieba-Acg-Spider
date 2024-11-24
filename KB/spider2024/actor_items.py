import scrapy

class actor_Item(scrapy.Item):
    name = scrapy.Field()
    birth_day = scrapy.Field()
    constellation = scrapy.Field()
    blood_type = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()