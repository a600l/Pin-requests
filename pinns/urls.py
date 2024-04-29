from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts', include('django.contrib.auth.urls')),  # Include accounts app's URLs
    path('', include('accounts.urls')),  # Include accounts app's URLs
    path('', include('core.urls')),  # Include core app's URLs
]
