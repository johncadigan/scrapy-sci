# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Wallpaper(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    origin = scrapy.Field()
    id = scrapy.Field()
    uploader = scrapy.Field()
    site = scrapy.Field()
    favorites = scrapy.Field()
    views = scrapy.Field()    
    download_link = scrapy.Field()
    colors = scrapy.Field()
    x_resolution = scrapy.Field()
    y_resolution = scrapy.Field()    
    descriptors = scrapy.Field()
    comments = scrapy.Field()

    

