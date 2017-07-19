from django import forms
from .models import Player_Attributes

class Player_AttributesForm(forms.ModelForm):
    class Meta:
        model = Player_Attributes
        # fields = ('username', 'skill_level', 'address', 'availability_days', 'availability_times', 'looking_for', 'phone_number', 'email', 'additional_info',)
        exclude = ('latitude', 'longitude')
