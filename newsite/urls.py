from django.conf.urls import url
from . import views

app_name = "newsite"
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/details/$', views.DetailView.as_view(), name = 'detail'),
      
]