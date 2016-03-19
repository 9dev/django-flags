from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return '<Article id={}>'.format(self.pk)
