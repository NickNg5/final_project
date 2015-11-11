from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
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

    def get_object(self, *args, **kwargs):
        object = super(BusinessUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class BusinessDeleteView(DeleteView):
    model = Business
    template_name = 'business/business_confirm_delete.html'
    success_url = reverse_lazy('business_list')

    def get_object(self, *args, **kwargs):
        object = super(BusinessDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

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

class CommentUpdateView(UpdateView):
    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'comment/comment_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.business.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(AnswerUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class CommentDeleteView(DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'comment/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.business.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(AnswerDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object