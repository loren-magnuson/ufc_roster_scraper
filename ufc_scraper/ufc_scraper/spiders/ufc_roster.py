# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from ufc_scraper.items import UfcFighterItem

class UfcRosterSpider(Spider):
    name = 'ufc_roster'
    allowed_domains = ['ufc.com']
    start_urls = ['http://www.ufc.com/fighter']

    def __init__(self):
        self.root_url = "http://www.ufc.com"

    def parse(self, response):
        for anchor in response.css("div.wc-classes-section a::attr(href)"):
            yield Request(url="%s/%s" % (self.root_url, anchor.extract()), callback=self.parse_division_page)

    def parse_division_page(self, response):
        for anchor in response.css("a.fighter-name::attr(href)"):
            yield Request(url="%s%s" % (self.root_url, anchor.extract()), callback=self.parse_fighter_page)

        pagination = response.css("ul.pagination a::attr(href)")
        if pagination:
            for anchor in pagination:
                yield Request(url="%s/%s" % (self.root_url, anchor.extract()), callback=self.parse_division_page)

    def parse_fighter_page(self, response):
        item = UfcFighterItem()
        item['url'] = response.url

        image = response.css("div.fighter-banner > div.fighter-image > img::attr(src)").extract_first()
        if image:
            item['image'] = "http://" + image

        name = response.css("#fighter-breadcrumb > span > h1::text").extract_first()
        if name:
            item['name'] = name

        quote = response.css("#fighter-details div.quote > blockquote > span::text").extract_first()
        if quote:
            item['quote'] = quote

        tables = response.css("tr")
        for row in tables:
            value = row.xpath('.//td[@class="value"]/text()').extract_first()
            id = row.xpath('.//td[@class="value"]/@id').extract_first()
            if not id or not value:
                continue
            else:
                id = id.replace("-", "_")
                if id in vars(UfcFighterItem)['fields']:
                    item[id] = value.replace("\t", "").replace("\n", "").strip()

        yield item

