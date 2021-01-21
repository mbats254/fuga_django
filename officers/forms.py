from django import forms
from .models import Officer

class RegisterOfficer(forms.Form):
    name = forms.CharField(label='Officers name')
    # email = forms.EmailField(label='Email')
    # county = forms.CharField(label='County')
    # id_no  = forms.IntegerField(label='ID No')
    # phone_no = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder': '0708323123'}))

    class Meta:
        model = Officer
        exclude = ['uniqid']