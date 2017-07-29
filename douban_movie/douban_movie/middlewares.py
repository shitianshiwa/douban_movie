# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from douban_movie.agents import agents


class UserAgentMiddleware(object):

	def process_request(self, request, spider):

		agent = random.choice(agents)
		request.headers['User-Agent'] = agent


