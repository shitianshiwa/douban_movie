# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import requests
from douban_movie.items import MovieItem

class MongoPipeline(object):
	def __init__(self, mongo_url, mongo_db):
		self.mongo_url = mongo_url
		self.mongo_db = mongo_db

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_url = crawler.settings.get('MONGO_URL'),
			mongo_db = crawler.settings.get('MONGO_DB')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_url)
		self.db = self.client[self.mongo_db]

	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item, spider):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
		img = requests.get(item['cover'], headers=headers)
		with open('E:/douban/{}/{}.jpg'.format(str(item['rate'])[0], item['title']), 'ab') as f:
			f.write(img.content)
			f.close()
		self.db['movie'].update({'id': item['id']}, {'$set': item}, True)
		return item
