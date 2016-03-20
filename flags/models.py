from django.conf import settings
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

    class Meta:
        unique_together = (('object_id', 'content_type', 'creator'),)


class Approve(models.Model):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    creator = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('object_id', 'content_type'),)


@receiver(post_save, sender=Approve)
def on_save_approve(sender, instance, **kwargs):\
    Flag.objects.filter(object_id=instance.object_id, content_type=instance.content_type).delete()


@receiver(post_save, sender=Flag)
def on_save_flag(sender, instance, **kwargs):
    try:
        Approve.objects.get(object_id=instance.object_id, content_type=instance.content_type)
        instance.delete()
    except Approve.DoesNotExist:
        flags = Flag.objects.filter(object_id=instance.object_id, content_type=instance.content_type)
        exists = flags.filter(creator=instance.creator).count() > 1

        if exists:
            instance.delete()
        else:
            threshold = getattr(settings, 'FLAGS_THRESHOLD', None)
            if threshold:
                count = flags.count()
                if count >= threshold:
                    instance.content_object.delete()
                    flags.delete()
