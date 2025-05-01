from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('apps.menus.urls')),
    path('promos/', include('apps.promos.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
