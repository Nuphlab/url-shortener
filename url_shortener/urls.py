from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import ShortenedURLViewSet

router = routers.DefaultRouter()
router.register(r'shortenedurls', ShortenedURLViewSet)

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten'),
    path('<str:short_url>/', views.get_original_url, name='get_original_url'),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'url_shortener.views.error_status_404'