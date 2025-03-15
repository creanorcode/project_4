from django.contrib import admin
from django.urls import path, include
from posts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Inloggning, utloggning etc.
    path('register/', register, name='register'),
    path('', include('posts.urls')),
]