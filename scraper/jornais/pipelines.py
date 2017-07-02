# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from newsite.models import Noticias
from datetime import datetime

class JornalPipeline(object):
    def process_item(self, item, spider):
        try:
        	news = Noticias.objects.get(link = item["link"])
        	return item
        
        except(Noticias.DoesNotExist):
        	pass

        image_link = item["image_link"]
        if(image_link == None):
        	image_link = "http://placeholders.org/320x200"
        new = Noticias(	title = item["title"],
        				image_link = image_link,
        				link = item["link"],
        				article = item["article"],
        				fonte = item["fonte"],
        				date = item["date"])
        new.save()
        return item

