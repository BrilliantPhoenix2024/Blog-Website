from django.shortcuts import render
from .models import My_design
from django.shortcuts import get_object_or_404


def home_page_view(request):
    return render(request, 'pages/home.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    return render(request, 'pages/contact.html')


def design_page_view(request):
    # designs_list = My_design.objects.all()
    designs_list = My_design.objects.filter(status='pub')
    return render(request, 'pages/design.html', {'designs_list': designs_list})


def services_page_view(request, pk):
    my_design = get_object_or_404(My_design, pk=pk)
    return render(request, 'pages/services.html', {'my_design': my_design})










