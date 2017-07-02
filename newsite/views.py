from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
#from scrapy.crawler import CrawlerRunner
from scraper.jornais.spiders.folha import FolhaSpider
from scraper.jornais.spiders.economia import EconomiaSpider
from .models import Noticias
from threading import Thread
# Create your views here.
import scrapydo
from time import sleep
scrapydo.setup()
scrapydo.default_settings.update({
    "USER_AGENT": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    "ROBOTSTXT_OBEY": True,
    "ITEM_PIPELINES": {
        'scraper.jornais.pipelines.JornalPipeline': 300,
    },
})

#def index(request):
#    return HttpResponse("VAI TOMAR NO CU")
    

def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    
    return decorator

@postpone
def update_db():
    scrapydo.run_spider(FolhaSpider)
    scrapydo.run_spider(EconomiaSpider)
    sleep(120)
    update_db()

class IndexView(generic.ListView):
    model = Noticias
    template_name = "newsite/index.html"
    context_object_name = "news"

    update_db()

    
    def get_queryset(self):
        return Noticias.objects.order_by("-date")

class DetailView(generic.DetailView):
    model = Noticias
    template_name = "newsite/detail.html"    
    context_object_name = "news"
    
