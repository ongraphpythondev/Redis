from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=3)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
