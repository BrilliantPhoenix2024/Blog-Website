from django.shortcuts import render
from .models import My_design


def home_page_view(request):
    return render(request, 'pages/home.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    return render(request, 'pages/contact.html')


def design_page_view(request):
    designs_list = My_design.objects.all()
    return render(request, 'pages/design.html', {'designs_list': designs_list})


def services_page_view(request):
    return render(request, 'pages/services.html')







