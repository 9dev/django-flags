from django.db import models
from django.core.urlresolvers import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '<Article id={}>'.format(self.pk)
