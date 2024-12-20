from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from uuid import UUID


urlpatterns = [
    path('chat/<int:user_id>/', views.chat_view, name='chat_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)