from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('vividvision/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
] 

