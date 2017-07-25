from django import template
from django.core.exceptions import ObjectDoesNotExist
register = template.Library()

@register.filter
def user_does_not_have_player_attributes(user):
    try:
        user.player_attributes
    except ObjectDoesNotExist:
        return True
    return False 
