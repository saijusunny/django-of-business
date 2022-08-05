from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('sale', views.sale, name='sale'),
    path('last', views.last, name='last'),
    
    
]