from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .models import Services


# Create your views here.
def index(request):
    banner_text = 'Excellence in Community Service'
    services = Services.objects.all().order_by('id')
    fixedBanner = False

    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':banner_text,
        'fixedBanner':fixedBanner,
    }

    return render(request, 'index.html', context)


def service(request, id):
    services = Services.objects.all().order_by('id')
    currentService = Services.objects.get(id=id)
    topView = currentService.topView
    listView = currentService.listView
    fixedBanner = True

    try:
        topView = topView.split(',')
    except AttributeError:
        pass
    
    try:
        listView = listView.split(',')
    except AttributeError:
        pass
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'currentService':currentService,
        'services':services,
        'bannerText':currentService.name,
        'topView':topView,
        'listView':listView,
        'fixedBanner':fixedBanner,
    }

    return render(request, 'service.html', context)


def covidStatement(request):
    services = Services.objects.all().order_by('id')
    fixedBanner = False
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':'Coronavirus (COVID-19) MayMaCare Community Services Statement',
        'fixedBanner':fixedBanner,
    }

    return render(request, 'covid-statement.html', context)


def requestCallback(request):
    services = Services.objects.all().order_by('id')
    fixedBanner = False
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':'Request Callback',
        'fixedBanner':fixedBanner,
    }

    return render(request, 'request.html', context)


def aboutUs(request):
    services = Services.objects.all().order_by('id')
    fixedBanner = False
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':'About Us',
        'fixedBanner':fixedBanner,
    }

    return render(request, 'about-us.html', context)


def contactUs(request):
    services = Services.objects.all().order_by('id')
    fixedBanner = False
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':'Contact Us',
        'fixedBanner':fixedBanner,
    }

    return render(request, 'contact-us.html', context)


def search(request):
    query = request.GET['q']
    services = Services.objects.all().order_by('id')
    searchResults = Services.objects.filter(name__icontains=query)
    fixedBanner = False
    
    context = {
        'company_name':settings.COMPANY_NAME,
        'contact_number_1':settings.CONTACT_NUMBER_1,
        'contact_number_2':settings.CONTACT_NUMBER_2,
        'address':settings.ADDRESS,
        'email':settings.EMAIL,
        'services':services,
        'bannerText':'Search Results',
        'searchResults':searchResults,
        'fixedBanner':fixedBanner,
    }

    return render(request, 'search.html', context)


def autosuggest(request):
    query = request.GET.get('term')
    searchResults = Services.objects.filter(name__icontains=query)
    suggestions = [x.name for x in searchResults]

    return JsonResponse(suggestions, safe=False)
