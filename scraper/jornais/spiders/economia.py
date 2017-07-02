# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scraper.jornais.items import NoticiaItem
from datetime import datetime

class EconomiaSpider(scrapy.Spider):
    name = 'economia'
    allowed_domains = ['economia.uol.com.br']
    start_urls = ['https://economia.uol.com.br/noticias//']

    def parse(self, response):
        news = response.xpath('//a[@class = "opacity-group"]')
        for item in news:
            title = item.xpath('span[@class = "h-opacity60 transition-050"]/text()').extract_first()
            link = item.xpath('@href').extract_first()
            yield Request(link, callback = self.parse_page, meta = {"title": title, "link": link})

    def parse_page(self, response):
        title = response.meta.get("title")
        link = response.meta.get("link")

        article = "".join(line for line in response.xpath('//div[@id="texto"]/text()').extract())
        article += "".join(line for line in response.xpath('//div[@id="texto"]/*/text()').extract())
        image_link = response.xpath('//img[@class = "imagem pinit-img"]/@src').extract_first()
        date = response.xpath('//div[@class = "info-header"]/time/@datetime').extract_first()

        new = NoticiaItem()
        new["title"] = title
        new["article"] = article
        new["link"] = link
        new["image_link"] = image_link
        new["date"] = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        new["fonte"] = "Economia UOL"

        return new

