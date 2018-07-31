from django.conf import settings
from django.db import models

from listings.models import Listing

# Create your models here.
class Event(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    listing         = models.ForeignKey(Listing)
    name            = models.CharField(max_length=120)
    description     = models.TextField(help_text='Event Description')
    lineup          = models.TextField(blank=True, null=True, help_text='Separate each act by comma.')
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']
