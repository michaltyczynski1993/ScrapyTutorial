from ast import parse
import scrapy

class WeatherScraper(scrapy.Spider):
    name = 'weather_spider'
    start_urls = ['https://pogoda.interia.pl/']

    def parse(self, response):

        current_weather = response.xpath('//*[@class = "weather-currently-temp-strict"]/text()').get()
        current_city = response.xpath('//h3[@class = "weather-currently-city"]/text()').get()
        perceptible = response.xpath('//*[@class = "weather-currently-details-value"]/text()').get()
        pressure = response.xpath('//*[@class = "weather-currently-details-value steady"]/text()').get()
        wind = response.xpath('//*[@class = "weather-currently-details-item wind"]/span/text()').get()
        # try:
        yield{
            'city': current_city.strip(),
            'weather': current_weather.strip(),
            'perceptible temperature': perceptible.strip(),
            'atmospheric pressure': pressure.strip(),
            'wind': wind.strip()
        }
        # except:
        #     yield{
        #         'city': current_city,
        #         'weather': current_weather,
        #         'perceptible temperature': perceptible,
        #         'atmospheric pressure': pressure,
        #         'wind': wind.strip()
        #     }

