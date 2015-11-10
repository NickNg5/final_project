from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
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

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'business/business_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BusinessDetailView, self).get_context_data(**kwargs)
        business = Business.objects.get(id=self.kwargs['pk'])
        comments = Comment.objects.filter(business=business)
        context['comments'] = comments
        return context

class BusinessUpdateView(UpdateView):
    model = Business
    template_name = 'business/business_form.html'
    fields = ['title', 'description']

class BusinessDeleteView(DeleteView):
    model = Business
    template_name = 'business/business_confirm_delete.html'
    success_url = reverse_lazy('business_list')

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/comment_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.business.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.business = Business.objects.get(id=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)

