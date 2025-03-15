from django.contrib import admin
from django.urls import path, include
from posts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inloggning, utloggning etc.
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', include('posts.urls')),
]
