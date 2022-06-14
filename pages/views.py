from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return render(request, 'pages/home.html')


def about_page_view(request):
    context = {
        'page_name': 'about',
        'description': 'this is s.th said in context',
        'button_value': "Dont click",
    }
    return render(request, 'pages/about.html', context)


def contact_page_view(request):
    return render(request, 'pages/contact.html')


def design_page_view(request):
    return render(request, 'pages/design.html')


def services_page_view(request):
    return render(request, 'pages/services.html')







