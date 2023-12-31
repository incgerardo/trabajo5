from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pag1"

    def start_requests(self):
        urls = [
            "https://www.flex.scoopforwork.com/explore?page=1"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }