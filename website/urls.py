from django.contrib import admin
from django.urls import path, include
from django.views.static import serve



urlpatterns = [
    path('vividvision/admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
] 




