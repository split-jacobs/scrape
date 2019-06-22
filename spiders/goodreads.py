import scrapy

class GoodReadsSpider(scrapy.Spider):
	#identity
	name = 'goodreads'
	
	#requests
	def start_requests(self):
		urls = [
		'https://www.fl.ru/projects/?page=1&kind=1',
		'https://www.fl.ru/projects/?page=2&kind=1',
		'https://www.fl.ru/projects/?page=3&kind=1'
		]
		
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	#response

	def parse (self, response):
		page_number = response.url.split("page=")[1].replace('&kind=1','')
		_file = "{0}.html".format(page_number)
		with open (_file , 'wb') as f:
			f.write(response.body)
