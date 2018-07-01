from django import forms
class Cities(forms.Form):
    city = forms.CharField(max_length = 20,
    widget = forms.TextInput(attrs={"placeholder":"Find your location..."}))
