# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class MusicItem(scrapy.Item):
    name = scrapy.Field()
    album = scrapy.Field()
    interval = scrapy.Field()
    href = scrapy.Field()
