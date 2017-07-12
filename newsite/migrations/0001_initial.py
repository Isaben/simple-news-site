# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_link', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('article', models.CharField(max_length=15000)),
                ('link', models.CharField(max_length=300)),
                ('fonte', models.CharField(max_length=50)),
            ],
        ),
    ]
