from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ListingCreateForm
from .models import Listing

# Create your views here.

def listing_createview(request):
    form = ListingCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/listings")
    if form.errors:
        errors = form.errors

    template_name = 'listings/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


def listings_listview(request):
    template_name = 'listings/listings_list.html'
    queryset = Listing.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

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
    queryset = Listing.objects.all()

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
