#this script intends to scrap information from second-hand websites on specific watch details such as title, price, brand, condition of watch
import scrapy
from scrapy.crawler import CrawlerProcess
import requests

#websites to scrap from
urls = ['https://www.ricardo.ch/de/s/garmin%20marq/']
website = requests.get(urls[0])
#initiat spider class
class garmin_marq_spider(scrapy.Spider):
    name = 'garmin_marq_spider'

    def start_request( self ):
        yield scrapy.Request(url = urls,
                         callback = self.parse_front)

    #parse follow-up urls from initial overview (multiple watches displayed on one page) 
    def parse_overview(self, response):
        watch_overview = response.xpath('//div[contains(@class, "MuiGrid-root container--2ZiLE MuiGrid-container MuiGrid-spacing-xs-2")]')
        watch_links = response.xpath('./a/@href')
        links_to_follow = watch_links.extract()
        for url in links_to_follow:
            response.follow(url = url,
                            callback = self.parse_details)

    #store information on details of watches
    def parse_details(self, response):
        watch_title = response.xpath('//h1[@class ="style_title__O6YYD"]/text()')
        watch_price = response.xpath('//div[@class ="jss77 style_price__2pp96"]/text()')
        watch_details = response.xpath('//p[@class = "jss77"]/text()')
        #strip unnecessary information from scrapped information
        watch_title_clean = watch_title.strip()
        watch_price_clean = watch_price.strip()
        watch_details_clean = watch_details.strip()
        return [watch_title_clean, watch_price_clean,watch_details_clean]

process = CrawlerProcess()
process.crawl(garmin_marq_spider)
process.start()
