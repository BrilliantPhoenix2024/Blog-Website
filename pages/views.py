from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse('home_page_view')

def about_page_view(request):
    return HttpResponse('about_page_view')

def contact_page_view(request):
    return HttpResponse('contact_page_view')

