from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Flag(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    creator = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(auto_now_add=True)


class Approve(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    creator = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Approve)
def my_callback(sender, instance, **kwargs):
    Flag.objects.filter(object_id=instance.object_id, content_type=instance.content_type).delete()
