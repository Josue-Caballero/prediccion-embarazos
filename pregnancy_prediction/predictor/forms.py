from django import forms

class DataForm(forms.Form):
    registries = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()
