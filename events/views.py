from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import EventForm
from .models import Event

class EventListView(ListView):

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventDetailView(DetailView):

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventCreateView(LoginRequiredMixin, CreateView):
    form_class = EventForm
    template_name = 'form.html'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(EventCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Event'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(EventCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EventForm
    template_name = 'form.html'
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(EventUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Event'
        return context

    def get_form_kwargs(self):
        kwargs = super(EventUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
