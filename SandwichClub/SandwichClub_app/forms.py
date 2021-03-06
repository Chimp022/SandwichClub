from django import forms
from SandwichClub_app.models import *

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwich
        exclude = ('sid','rating','created','maker')
