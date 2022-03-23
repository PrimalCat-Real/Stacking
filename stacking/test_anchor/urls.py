from xml.dom.minidom import Document
from django.urls import path
from django.conf.urls.static import static
from .views import *
from django.conf import settings


urlpatterns = [
    path('', anchor),
    path('test/', test),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
