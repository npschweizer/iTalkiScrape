from scrapy import Spider
from italki.items import iTalkiTeacher

class iTalkiTeacherSpider(Spider):
	name = 'iTalki_Teacher_Spider'
	allowed_urls = ['https://italki.com']
	start_urls = ['https://www.italki.com/teachers/english'] #can have more than one of these apparently
					https://www.italki.com/teachers/chinese
					/french
					/spanish
					/portugese
					/german	
					/japanese
					/korean
					/arabic
					/hindi
					/italian
					/russian

	def parse(self, response):
	rows = response.xpath('//*[@id=".teacher-card-left"]')

	for row in rows:


		for pattern in patterns:
