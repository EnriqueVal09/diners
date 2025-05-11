from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('menu/', include('apps.menus.urls')),
    path('promos/', include('apps.promos.urls')),
    path('admin/', admin.site.urls),
    #path("__reload__/", include("django_browser_reload.urls")),
]
# use media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
