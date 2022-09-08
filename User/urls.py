from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('covid-statement', views.covidStatement, name='covid'),
    path('search', views.search, name='search'),
    path('autosuggest', views.autosuggest, name='autosuggest'),
    path('about-us', views.aboutUs, name='aboutUs'),
    path('contact-us', views.contactUs, name='contactUs'),
    path('request-call-back', views.requestCallback, name='requestCallback'),
    path('services/<id>', views.service, name='service'),
]
