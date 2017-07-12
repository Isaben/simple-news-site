# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scraper.jornais.items import NoticiaItem
from datetime import datetime

class FolhaSpider(scrapy.Spider):
    name = 'folha'
    allowed_domains = ['folha.uol.com.br']
    start_urls = ['http://www1.folha.uol.com.br/poder//']

    def parse(self, response):

        news = response.xpath('//li[@class = "latest-news-list-item"]')
        
        for item in news:
            title = item.xpath('.//h3/text()').extract_first()
            date = item.xpath('.//time/@datetime').extract_first()
            link = item.xpath('.//a/@href').extract_first()

            yield Request(link, callback = self.parse_page, meta = {"title": title, "date": date, "link": link})

        news_old = response.xpath('//ol[@class = "unstyled"]')
        for item in news_old:
            temp = item.xpath('.//li')
            for inside in temp:
                title = inside.xpath('a/text()').extract_first()
                link = inside.xpath('a/@href').extract_first()
                date = inside.xpath('time/@datetime').extract_first()

                yield Request(link, callback = self.parse_page, meta = {"title": title, "date": date, "link": link})
            

    def parse_page(self, response):
        title = response.meta.get("title")
        link = response.meta.get("link")
        date = response.meta.get("date")

        image_link = response.xpath('//td[@class = "articleGraphicImage"]/img/@src').extract_first()
        article = "".join(line for line in response.xpath('//*[@itemprop="articleBody"]/p/text()').extract())

        new = NoticiaItem()
        new["title"] = title
        new["article"] = article
        new["link"] = link
        new["image_link"] = image_link
        new["date"] = datetime.strptime(date, "%Y-%m-%d %H:%M")
        new["fonte"] = "Folha de São Paulo"
        return new