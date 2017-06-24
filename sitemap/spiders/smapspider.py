import scrapy
from scrapy.spiders import SitemapSpider
import json
import os 

class SmapSpider(SitemapSpider):
    name="sitemap"
    sitemap_urls = ['http://www.rappler.com/sitemap-2015.xml']
    count = 0
    count_max = 20
    data = {}
    data['sitemap'] = []

    def parse(self,response):
        if self.count < self.count_max:
            self.count = self.count + 1
            self.data['sitemap'].append({"url": response.url})
            scrapy.Request(response.url, callback=self.parse)
            
        else:
            with open('result.json', 'w') as outfile:  
                json.dump(self.data, outfile)
            os._exit(1)

