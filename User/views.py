from django.http import JsonResponse
from django.shortcuts import render
from .models import Services


# Create your views here.
def index(request):
    company_name = 'MayMaCare'
    banner_text = 'Excellence in Community Service'
    services = Services.objects.all()

    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':banner_text,
    }
    
    return render(request, 'index.html', context)


def service(request, id):
    company_name = 'MayMaCare'
    services = Services.objects.all()
    currentService = Services.objects.get(id=id)
    topView = currentService.topView
    listView = currentService.listView

    try:
        topView = topView.split(',')
    except AttributeError:
        pass
    
    try:
        listView = listView.split(',')
    except AttributeError:
        pass
    
    context = {
        'company_name':company_name,
        'currentService':currentService,
        'services':services,
        'bannerText':currentService.name,
        'topView':topView,
        'listView':listView
    }

    return render(request, 'service.html', context)


def covidStatement(request):
    company_name = 'MayMaCare'
    services = Services.objects.all()
    
    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':'Coronavirus (COVID-19) MayMaCare Community Services Statement',
    }

    return render(request, 'covid-statement.html', context)


def requestCallback(request):
    company_name = 'MayMaCare'
    services = Services.objects.all()
    
    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':'Request Callback',
    }

    return render(request, 'request.html', context)


def aboutUs(request):
    company_name = 'MayMaCare'
    services = Services.objects.all()
    
    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':'About Us',
    }

    return render(request, 'about-us.html', context)


def contactUs(request):
    company_name = 'MayMaCare'
    services = Services.objects.all()
    
    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':'Contact Us',
    }

    return render(request, 'contact-us.html', context)


def search(request):
    company_name = 'MayMaCare'
    query = request.GET['q']
    services = Services.objects.all()
    searchResults = Services.objects.filter(name__icontains=query)
    
    context = {
        'company_name':company_name,
        'services':services,
        'bannerText':'Search Results',
        'searchResults':searchResults
    }

    return render(request, 'search.html', context)


def autosuggest(request):
    query = request.GET.get('term')
    searchResults = Services.objects.filter(name__icontains=query)
    suggestions = [x.name for x in searchResults]

    return JsonResponse(suggestions, safe=False)
