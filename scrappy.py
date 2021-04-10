
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.idees-gages.com/mots-jeu-pendu.php']

    def parse(self, response):
        for title in response.css('div#mw-pages div.mw-content-ltr li''):
            yield ['title': title.css('::text').get()]
