from django.urls import path
from .views import discussions_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', discussions_view, name='discussions_view'),  # Root of the discussions app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
