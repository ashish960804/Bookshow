from django.conf.urls import url
from home import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.show_index, name='show_index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    ]
    

