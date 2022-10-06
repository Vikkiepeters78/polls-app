from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
