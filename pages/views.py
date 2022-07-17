from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .models import My_design
from .forms import DesignForm


def home_page_view(request):
    return render(request, 'pages/home.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    return render(request, 'pages/contact.html')


class DesignListView(generic.ListView):
    # model = My_design
    template_name = 'pages/design.html'
    context_object_name = 'designs_list'

    def get_queryset(self):
        return My_design.objects.filter(status='pub').order_by('-datetime_modified')


class DesignDetailview(generic.DetailView):
    model = My_design
    template_name = 'pages/detail_design.html'
    context_object_name = 'my_design'


class DesignCreateView(generic.CreateView):
    form_class = DesignForm
    template_name = 'pages/create_design.html'


class DesignUpdateView(generic.UpdateView):
    model = My_design
    form_class = DesignForm
    template_name = 'pages/create_design.html'


class DesignDeleteView(generic.DeleteView):
    model = My_design
    template_name = 'pages/delete_design.html'
    success_url = reverse_lazy('design')

# def design_page_view(request):
#     # designs_list = My_design.objects.all()
#     designs_list = My_design.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'pages/design.html', {'designs_list': designs_list})


# def detail_design_page_view(request, pk):
#     my_design = get_object_or_404(My_design, pk=pk)
#     return render(request, 'pages/detail_design.html', {'my_design': my_design})


# def create_design_page_view(request):
#     if request.method == 'POST':
#         form = DesignForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = DesignForm()
#             return redirect('design')
#
#     else:  # GET request
#         form = DesignForm()
#
#     return render(request, 'pages/create_design.html', context={'form': form})
    # if request.method == 'POST':
    #     design_title = request.POST.get('title')
    #     design_description = request.POST.get('des')
    #
    #     user = User.objects.all()[0] #django ORM
    #     My_design.objects.create(title=design_title, description=design_description, author=user, status='pub')
    # else:
    #     print('GET request')
    # return render(request, 'pages/create_design.html')


# def design_update_view(request, pk):
#     design = get_object_or_404(My_design, pk=pk)
#     form = DesignForm(request.POST or None, instance=design)
#
#     if form.is_valid():
#         form.save()
#         return redirect('design')
#
#     return render(request, 'pages/create_design.html', context={'form': form})


# def design_delete_view(request, pk):
#     design = get_object_or_404(My_design, pk=pk)
#
#     if request.method == 'POST':
#         design.delete()
#         return redirect('design')
#
#     return render(request, 'pages/delete_design.html', context={'design': design})















