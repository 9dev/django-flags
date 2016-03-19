from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def flag_create_url(obj):
    return reverse('flags:flag_create', kwargs={
        'app_name': obj._meta.app_label,
        'model_name': obj._meta.object_name.lower(),
        'pk': obj.pk
    })
