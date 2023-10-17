from django import forms

class formconverter(forms.Form):
    num1 = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={"placeholder": "Número a convertir", "class": "forms"}))
    num2 = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={"placeholder": "Número a convertir", "class": "forms"}))
    num3 = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={"placeholder": "Número a convertir", "class": "forms"}))
    num4 = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={"placeholder": "Número a convertir", "class": "forms"}))
    num5 = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={"placeholder": "Número a convertir", "class": "forms"}))