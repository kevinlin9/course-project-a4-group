from django import forms
from .models import buyNow
from django.forms import ModelForm

class buyNowForm(ModelForm):
    class Meta:
        model = buyNow
        fields = [
            'username','fullName', 'address1', 'address2', 'zip_code', 'city', 'item'
            ]