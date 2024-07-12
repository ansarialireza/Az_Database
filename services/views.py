from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.views.generic import ListView
from .models import *
from django.views.generic import DetailView
from .query_manager import ServicesQueryManager


class ServicesListView(ListView):
    model = Services
    template_name = 'services/services_home.html'
    context_object_name = 'services'
    paginate_by = 6

    def get_queryset(self):
        cat_name = self.kwargs.get('cat_name')
        username = self.kwargs.get('username')
        tag_name = self.kwargs.get('tag_name')

        queryset = ServicesQueryManager.get_all_services(cat_name, username, tag_name)

        return queryset

class ServicesDetailView(DetailView):
    model = Services
    template_name = 'services/service-single.html'
    context_object_name = 'post'


class ServicesSearchView(ListView):
    template_name = 'services/services_home.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('s')  # Retrieve the 's' parameter from the GET request

        if query:
            queryset = ServicesQueryManager.search_services(query)
        else:
            queryset = ServicesQueryManager.get_all_services()

        return queryset