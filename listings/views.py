from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import ListingCreateForm
from .models import Listing

# Create your views here.

class ListingListview(ListView):
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Listing.objects.filter(
            Q(category__iexact=slug) |
            Q(category__icontains=slug)
            )
        else:
            queryset = Listing.objects.all()
        return queryset

class ListingDetailview(DetailView):
        def get_queryset(self):
            return Listing.objects.all()

    # def get_object(self, *args, **kwargs):
    #     listing_id = self.kwargs.get('listing_id')
    #     obj = get_object_or_404(Listing, id=listing_id )
    #     return obj

class ListingCreateView(LoginRequiredMixin, CreateView):
    form_class = ListingCreateForm
    template_name = 'listings/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ListingCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ListingCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Rooftop'
        return context

class ListingUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ListingCreateForm
    template_name = 'listings/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListingUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Rooftop'
        return context
