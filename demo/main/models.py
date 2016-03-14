from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
