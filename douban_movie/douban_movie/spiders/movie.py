# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from douban_movie.items import MovieItem
import json
from copy import deepcopy
from urllib.parse import urlencode


class MovieSpider(Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com', 'img1.doubanio.com']
    start_urls = ['http://movie.douban.com/']
    header_url = 'https://movie.douban.com/j/new_search_subjects?'
    tags = ["大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","西班牙","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]

    def start_requests(self):
    	data = {
    		'sort': 'T',
    		'range': '0,10',
    		'tags': '',
    		'start': 0,
    	}
    	for tag in self.tags:
    		data['tags'] = '电影,' + tag
    		url = self.header_url + urlencode(data)
    		yield Request(url=url, meta=deepcopy({'data': data, 'area': tag}), callback=self.parse_page)

    def parse_page(self, response):
        meta = response.meta
        meta['data']['start'] += 20
        movie_datas = json.loads(response.text)
        item = MovieItem()

        if movie_datas['data']:

        	for movie_data in movie_datas['data']:
        		item['area'] = response.meta['area']
        		for field in item.fields:
        			if field in movie_data.keys():
        				item[field] = movie_data.get(field)
        		yield item
        	url = self.header_url + urlencode(meta['data'])
        	yield Request(url=url, meta=deepcopy(meta), callback=self.parse_page)

