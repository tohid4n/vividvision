from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('tohid/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
]

