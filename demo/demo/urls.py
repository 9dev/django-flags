from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from flags import urls as flags_urls

from main import urls as main_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flags/', include(flags_urls, namespace='flags')),
    url(r'', include(main_urls)),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

