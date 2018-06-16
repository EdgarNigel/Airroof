from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from. validators import validate_category

# Create your models here.
class Listing(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True)
    category    = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name

    # title needed for unique slug generator (instance.title)
    @property
    def title(self):
        return self.name #ability to add obj.title

def listing_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def listing_post_save_receiver(sender, instance, *args, **kwargs):
#     print('saved..')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(listing_pre_save_receiver, sender=Listing)

# post_save.connect(listing_post_save_receiver, sender=Listing)
