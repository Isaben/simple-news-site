from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import scrapy
#from scrapy.crawler import CrawlerRunner
from scraper.jornais.spiders.folha import FolhaSpider
from scraper.jornais.spiders.economia import EconomiaSpider
from .models import Noticias
from datetime import datetime
from twisted.internet import reactor

from scrapy import signals
from scrapy.crawler import CrawlerRunner
# Create your views here.
import scrapydo
scrapydo.setup()

scrapydo.default_settings.update({
    "USER_AGENT": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    "ROBOTSTXT_OBEY": True,
    "ITEM_PIPELINES": {
        'scraper.jornais.pipelines.JornalPipeline': 300,
    },
})
"""def index(request):
    return HttpResponse("VAI TOMAR NO CU")
    """
class IndexView(generic.ListView):
    model = Noticias
    template_name = "newsite/index.html"
    context_object_name = "news"


    """runner = CrawlerRunner(settings = {
        "USER_AGENT": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        "ROBOTSTXT_OBEY": True,
        "ITEM_PIPELINES": {
            'scraper.jornais.pipelines.JornalPipeline': 300,
        },


        })

    d = self.runner.crawl(FolhaSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers = 0) # the script will block here until the crawling is finished"""
    
    def get_queryset(self):
        scrapydo.run_spider(FolhaSpider)

        return Noticias.objects.order_by("-date")

class DetailView(generic.DetailView):
    model = Noticias
    template_name = "newsite/detail.html"    
    context_object_name = "news"
