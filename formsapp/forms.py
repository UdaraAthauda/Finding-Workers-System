from django import forms
from django.forms import ModelForm
from .models import WorkerDetails

class Registration(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.IntegerField(label='Contact Number (Ex: 071xxxxxxx)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    confpass = forms.CharField(label='Confirm Password', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))


class Login(forms.Form):
    contact = forms.IntegerField(label='Contact Number (Ex: 071xxxxxxx)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))


class WorkerDetailForm(ModelForm):
    class Meta:
        model = WorkerDetails
        fields = ('First_name', 'Last_name', 'Worker_image', 'Contact_number', 'Location', 'Working_areas', 'Experience', 'Description')

    def __init__(self, *args, **kwargs):
        super(WorkerDetailForm, self).__init__(*args, **kwargs)
        self.fields['First_name'].widget.attrs['class'] = 'form-control'
        self.fields['Last_name'].widget.attrs['class'] = 'form-control'
        self.fields['Worker_image'].widget.attrs['class'] = 'form-control'
        self.fields['Contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['Location'].widget.attrs['class'] = 'form-control'
        self.fields['Working_areas'].widget.attrs['class'] = 'form-control'
        self.fields['Experience'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'