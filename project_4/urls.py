# PRoject_4/urls.py

# Import Django´s admin module and URL utilities
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Import the custom registration view from posts
from posts.views import register

urlpatterns = [
    # Admin URL for Django admin interface
    path('admin/', admin.site.urls),
    # URL patterns for built-in Django authentication
    # (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Registration URL using a custom register view
    path('register/', register, name='register'),
    # Include URL patterns for the main application from the posts app
    path('', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
