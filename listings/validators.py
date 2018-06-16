from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

CATEGORIES = ['Private', 'Commercial']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")
