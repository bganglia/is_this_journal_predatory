#This is missing the code to actually calls the scraper, but you get the idea

import scrapy

class PredatorySpider(scrapy.Spider):
    name = "predatory"

    def start_requests(self):
        url="https://beallslist.net/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        out = {}
        sites = response.selector.xpath("//div[@class='wp-block-column']/ul/li")
        for idx, site in enumerate(sites):
            url=site.xpath("a/@href").getall()
            name=site.xpath("a/text()").getall()
            notes=site.xpath("*[position>1]").getall()
            out[idx] = {"url":url,
                        "name":name,
                        "notes":notes
                       }
        return out
