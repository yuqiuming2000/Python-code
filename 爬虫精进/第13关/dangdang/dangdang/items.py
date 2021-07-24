import scrapy
#导入scrapy
class dangdangItem(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    price_n = scrapy.Field()
    price_r = scrapy.Field()
    price_s = scrapy.Field()
    title= scrapy.Field()
