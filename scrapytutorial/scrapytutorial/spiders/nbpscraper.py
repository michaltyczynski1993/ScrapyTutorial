import scrapy


class NbpScraper(scrapy.Spider):
    name = 'nbpscraper'
    start_urls = ['https://www.nbp.pl/']

    def parse(self, response):
        table = response.xpath('//*[@id = "rightSide"]/table[2]//tr')
        for row in table:
            yield{
                'currency': row.xpath('./td[1]/text()').get(),
                'value': row.xpath('./td[2]/text()').get(),
            }
