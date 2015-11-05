from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
    template_name = 'home.html'

class BusinessCreateView(CreateView):
    model = Business
    template_name = 'business/business_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('business_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BusinessCreateView, self).form_valid(form)


class BusinessListView(ListView):
    model = Business
    template_name = 'business/business_list.html'
