from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter product's name"
        }
    ))
    description = forms.CharField(label="Name", widget=forms.Textarea(
        attrs={
            'placeholder': "Enter product's description",
            'rows':2,
            'cols':22.5,
            'class': 'mb-3',
            'id':'my-id'
        }
    ))
    price = forms.DecimalField(label="Name", initial=0.00)
    #image = forms.ImageField()
    status = forms.BooleanField(label="Status", required=False)
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'status')





class RowProductForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter product's name"
        }
    ))
    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'placeholder': "Enter product's description",
            'rows':2,
            'cols':22.5,
            'class': 'mb-3',
            'id':'my-id'
        }
    ))
    price = forms.DecimalField(label="", initial=0.00)
    #image = forms.ImageField()
    status = forms.BooleanField(label="Status", required=False)
    


