from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import Noticias
from datetime import datetime
# Create your views here.

"""def index(request):
    return HttpResponse("VAI TOMAR NO CU")
    """
class IndexView(generic.ListView):
    model = Noticias
    template_name = "newsite/index.html"
    context_object_name = "news"

    def get_queryset(self):
        return Noticias.objects.order_by("-date")

class DetailView(generic.DetailView):
    model = Noticias
    template_name = "newsite/detail.html"    
    context_object_name = "news"

def update_list():

    data = open("newsite/result.json", 'r')
    temp = ""
    for line in data:
        temp += line
    
    parsed = json.loads(temp)

    for news in parsed:
        title = news["Title"].replace("\t", "").replace("\n", "")
        image_link = news["image_link"]
        if(image_link == None):
            image_link = "http://dhiglobal.com/wp-content/uploads/2016/07/placeholder.jpg"
        date = datetime.strptime(news["date"], "%Y-%m-%d %H:%M")
        article = news["article"]
        link = news["link"]
        source = news["fonte"]
        temp = Noticias(title = title, image_link = image_link, date = date, article = article, link = link, fonte = source)
        temp.save()