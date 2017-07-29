# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
	title = scrapy.Field()
	rate = scrapy.Field()
	directors = scrapy.Field()
	area = scrapy.Field()
	casts = scrapy.Field()
	url = scrapy.Field()
	cover = scrapy.Field()
	id = scrapy.Field()
