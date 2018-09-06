from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from listings.models import Listing

# Create your models here.
class Event(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    listing         = models.ForeignKey(Listing)
    name            = models.CharField(max_length=120)
    description     = models.TextField(help_text='Event Description')
    tags            = models.TextField(blank=True, null=True, help_text='Divide Tags by comma')
    lineup          = models.TextField(blank=True, null=True, help_text='Separate each act by comma.')
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_tags(self):
        return self.tags.split(',')

    def get_lineup(self):
        return self.lineup.split(',')
