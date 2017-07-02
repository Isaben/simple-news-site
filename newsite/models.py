from django.db import models

# Create your models here.
class Noticias(models.Model):

    title = models.CharField(max_length = 200)
    image_link = models.CharField(max_length = 500)
    date = models.DateTimeField()
    article = models.CharField(max_length = 15000)
    link = models.CharField(max_length = 300)
    fonte = models.CharField(max_length = 50)

    def __str__(self):
        return ("Título: "+ self.title + "/ Fonte: " + self.fonte)
    